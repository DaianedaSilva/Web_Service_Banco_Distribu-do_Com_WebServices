from requestFilter import api_required
from flask import Flask, request
from datetime import datetime
import requests
import logging
import json

# Inicialização dos dados base para o servidor
tokenCliente1 = "6f986d8b-7cd7-4a2b-b645-5791f7b52ea8"
tokenCliente2 = "6a7de581-54d1-4e49-be22-128a00d958b8"
tokenCliente3 = "14457e72-720f-4afa-86a1-08c646aef0fb"
tokenCliente4 = "7ba5640b-3a25-4ecc-9a6e-9c9a129f2cb6"
tokenCliente5 = "29d0de06-6fad-4b8b-bbfe-bba2cc2c6297"
tokenCliente6 = "05281ee0-0bad-4eca-bab1-0fe76f8eb688"

tokens = [tokenCliente1, tokenCliente2, tokenCliente3,
          tokenCliente4, tokenCliente5, tokenCliente6]

operacoes = 0

dataServer = "http://localhost:5000/"
lock = "/lock"
unlock = "/unlock"
headers = {"x-api-key": "854d6b6a-04d4-42d4-a440-8c45eca2f610"}

# Configurações do servidor
logging.basicConfig(filename='logs.log', level=logging.DEBUG)
app = Flask(__name__)
app.run(debug=True, port=5003)

# Funções base


def _lockConta(acnt):
    return requests.post(url=dataServer+acnt+lock, headers=headers)


def _unlockConta(acnt):
    return requests.post(url=dataServer+acnt+unlock, headers=headers)


def _getSaldo(acnt):
    return requests.get(url=dataServer+acnt, headers=headers)


def _setSaldo(acnt, amt):
    return requests.post(url=dataServer+acnt+'/'+amt, headers=headers)

# Rotas web


@app.route('/deposito/<acnt>/<amt>', methods=['POST'])
@api_required
def deposito(acnt, amt):
    id_cliente = tokens.index(request.headers.get("x-api-key")) + 1

    if(int(amt) <= 0):
        return{"mensagem": "Valor inválido"}, 400

    lockResponse = _lockConta(acnt)
    if(lockResponse.status_code != 200):
        return lockResponse.content, lockResponse.status_code

    depositoResponse = _setSaldo(acnt, amt)
    if (depositoResponse.status_code != 200):
        return depositoResponse.content, depositoResponse.status_code

    global operacoes
    operacoes = operacoes + 1
    logging.info("TIMESTAMP: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") +
                 " NumOperação: " + str(operacoes) +
                 " ID Cliente: " + str(id_cliente) +
                 " TipoOperação: " + "deposito" +
                 " Conta: " + str(acnt) +
                 " Valor: " + str(amt))

    unlockRespoonse = _unlockConta(acnt)

    return depositoResponse.content, depositoResponse.status_code


@app.route('/saque/<acnt>/<amt>', methods=['POST'])
@api_required
def saque(acnt, amt):
    id_cliente = tokens.index(request.headers.get("x-api-key")) + 1

    if(int(amt) <= 0):
        return{"mensagem": "Valor inválido"}, 400

    saldoResponse = _getSaldo(acnt)
    if (saldoResponse.status_code != 200):
        return saldoResponse.content, saldoResponse.status_code

    saldoConta = int(json.loads(saldoResponse.text)["Saldo"])

    if(int(int(amt) > saldoConta)):
        return{"mensagem": "Saldo insuficiente"}, 400

    lockResponse = _lockConta(acnt)
    if(lockResponse.status_code != 200):
        return lockResponse.content, lockResponse.status_code

    saqueResponse = _setSaldo(acnt, str(int(amt)*-1))
    if (saqueResponse.status_code != 200):
        return saqueResponse.content, saqueResponse.status_code

    global operacoes
    operacoes = operacoes + 1
    logging.info("TIMESTAMP: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") +
                 " NumOperação: " + str(operacoes) +
                 " ID Cliente: " + str(id_cliente) +
                 " TipoOperação: " + "deposito" +
                 " Conta: " + str(acnt) +
                 " Valor: " + str(amt))

    unlockRespoonse = _unlockConta(acnt)

    return saqueResponse.content, saqueResponse.status_code


@app.route('/saldo/<acnt>', methods=['GET'])
@api_required
def saldo(acnt):
    id_cliente = tokens.index(request.headers.get("x-api-key")) + 1

    saldoResponse = _getSaldo(acnt)
    if saldoResponse.status_code != 200:
        return saldoResponse.content, saldoResponse.status_code

    global operacoes
    operacoes = operacoes + 1
    logging.info("TIMESTAMP: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") +
                 " NumOperação: " + str(operacoes) +
                 " ID Cliente: " + str(id_cliente) +
                 " TipoOperação: " + "saldo" +
                 " Conta: " + str(acnt))

    return saldoResponse.content, saldoResponse.status_code


@app.route('/transferencia/<acnt_orig>/<acnt_dest>/<amt>', methods=['POST'])
@api_required
def transferencia(acnt_orig, acnt_dest,  amt):
    id_cliente = tokens.index(request.headers.get("x-api-key")) + 1

    if(int(amt) <= 0):
        return{"mensagem": "Valor inválido"}, 400

    saldoResponse1 = _getSaldo(acnt_orig)
    if(saldoResponse1.status_code != 200):
        return saldoResponse1.content, saldoResponse1.status_code

    saldoConta1 = int(json.loads(saldoResponse1.text)["Saldo"])
    if(int(amt) > saldoConta1):
        return{"mensagem": "Saldo insuficiente"}, 400

    lockRespopnse1 = _lockConta(acnt_orig)
    if(lockRespopnse1.status_code != 200):
        return lockRespopnse1.content, lockRespopnse1.status_code

    lockRespopnse2 = _lockConta(acnt_dest)
    if(lockRespopnse2.status_code != 200):
        unlockRespoonse2 = _unlockConta(acnt_orig)
        return lockRespopnse2.content, lockRespopnse2.status_code

    saqueResponse = _setSaldo(acnt_orig, str(int(amt)*-1))
    if saqueResponse.status_code != 200:
        return saqueResponse.content, saqueResponse.status_code

    depositoResponse = _setSaldo(acnt_dest, str(int(amt)))
    if depositoResponse.status_code != 200:
        depositoResponse = _setSaldo(acnt_orig, str(int(amt)))
        return depositoResponse.content, depositoResponse.status_code

    global operacoes
    operacoes = operacoes + 1

    logging.info("TIMESTAMP: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") +
                 " NumOperação: " + str(operacoes) +
                 " ID Cliente: " + str(id_cliente) +
                 " TipoOperação: " + "deposito" +
                 " Conta1: " + str(acnt_orig) +
                 " Conta2: " + str(acnt_dest) +
                 " Valor: " + str(amt))
    saldoConta1 = int(json.loads(saqueResponse.text)["Saldo"])
    saldoConta2 = int(json.loads(depositoResponse.text)["Saldo"])
    unlockRespoonse1 = _unlockConta(acnt_orig)
    unlockRespoonse2 = _unlockConta(acnt_dest)

    return {"Saldo1": saldoConta1, "Saldo2": saldoConta2}, 200

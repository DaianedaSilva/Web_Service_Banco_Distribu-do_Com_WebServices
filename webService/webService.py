from requestFilter import api_required
from flask import Flask, request
from datetime import datetime
import requests
import logging

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
headers = {"x-api-key": "9cdcaba2-2e76-4a34-ae0a-3b3d54e0002d"}

# Configurações do servidor
logging.basicConfig(filename='logs.log', level=logging.DEBUG)
app = Flask(__name__)
app.run(debug=True, port=5001)

# Funções base
def _lockConta(acnt):
    return requests.post(url=dataServer+acnt+lock, headers=headers)

def _unlockConta(acnt):
    return requests.post(url=dataServer+acnt+unlock, headers=headers)

def _setSaldo(acnt):
    return requests.get(url=dataServer+acnt, headers=headers)

def _setSaldo(acnt,amt):
    return requests.post(url=dataServer+acnt+'/'+amt, headers=headers)

# Rotas web
@app.route('/deposito/<acnt>/<amt>', methods=['POST'])
@api_required
def deposito(acnt, amt):
    id_cliente = tokens.index(request.headers.get("x-api-key")) + 1

    if(int(amt)<= 0 ):
        return{"mensagem":"Valor inválido"}, 400

    lockRespopnse = _lockConta(acnt)
    if(lockRespopnse.status_code != 200):
        return {"mensagem": "Conta bloqueada"}, 423

    global operacoes
    operacoes = operacoes + 1
    depositResponse = _setSaldo(acnt,amt)
    logging.info("TIMESTAMP: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") +
                 " NumOperação: " + str(operacoes) +
                 " ID Cliente: " + str(id_cliente) +
                 " TipoOperação: " + "deposito" +
                 " Conta: " + str(acnt) +
                 " Valor: " + str(amt))

    unlockRespoonse = _unlockConta(acnt)

    return depositResponse.content, 200


@app.route('/saque/<acnt>/<amt>', methods=['POST'])
@api_required
def saque(acnt, amt):
    str = 'saque de ' + acnt + ' para' + amt
    logging.info(str)
    return str


@app.route('/saldo/<acnt>', methods=['GET'])
@api_required
def saldo(acnt):
    str = 'Saldo de ' + acnt
    logging.info(str)
    return str


@app.route('/transferencia/<acnt_orig>/<acnt_dest>/<amt>', methods=['POST'])
@api_required
def transferencia(acnt_orig, acnt_dest,  amt):
    str = 'transferencia de ' + acnt_orig + \
        " para " + acnt_dest + " no valor de " + amt
    logging.info(str)
    return str

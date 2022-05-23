import requests
import json

Cliente1 = "6f986d8b-7cd7-4a2b-b645-5791f7b52ea8"
Cliente2 = "6a7de581-54d1-4e49-be22-128a00d958b8"
Cliente3 = "14457e72-720f-4afa-86a1-08c646aef0fb"
Cliente4 = "7ba5640b-3a25-4ecc-9a6e-9c9a129f2cb6"
Cliente5 = "29d0de06-6fad-4b8b-bbfe-bba2cc2c6297"
Cliente6 = "05281ee0-0bad-4eca-bab1-0fe76f8eb688"

clientes = [Cliente1, Cliente2, Cliente3,
          Cliente4, Cliente5, Cliente6]

server1 = "http://localhost:5001/"
server2 = "http://localhost:5002/"
server3 = "http://localhost:5003/"
servers = [server1,server2,server3]




def deposito(conta, valor):
    requisição = requests.post(
        url=urlBase+"deposito/"+str(conta)+"/"+str(valor), headers=tokenCliente)

    if(requisição.status_code == 200):
        resultado = json.loads(requisição.text)["Saldo"]
        print(f"Sucesso:: Novo saldo da conta {conta}:{resultado}")
    else:
        resultado = json.loads(requisição.text)["mensagem"]
        print(f"Falha::{resultado}")


def saque(conta, valor):
    requisição = requests.post(
        url=urlBase+"saque/"+str(conta)+"/"+str(valor), headers=tokenCliente)

    if(requisição.status_code == 200):
        resultado = json.loads(requisição.text)["Saldo"]
        print(f"Sucesso:: Novo saldo da conta {conta}:{resultado}")
    else:
        resultado = json.loads(requisição.text)["mensagem"]
        print(f"Falha::{resultado}")


def transferencia(conta1, conta2, valor):
    requisição = requests.post(
        url=urlBase+"transferencia/"+str(conta1)+"/"+str(conta2)+"/"+str(valor), headers=tokenCliente)

    if(requisição.status_code == 200):
        resultado = json.loads(requisição.text)["Saldo1"]
        print(f"Sucesso:: Novo saldo da conta {conta1}:{resultado}")
        resultado = json.loads(requisição.text)["Saldo2"]
        print(f"Sucesso:: Novo saldo da conta {conta2}:{resultado}")
    else:
        resultado = json.loads(requisição.text)["mensagem"]
        print(f"Falha::{resultado}")


def saldo(conta):
    requisição = requests.get(
        url=urlBase+"saldo/"+str(conta), headers=tokenCliente)

    if(requisição.status_code == 200):
        resultado = json.loads(requisição.text)["Saldo"]
        print(f"Sucesso:: Saldo da conta {conta}:{resultado}")
    else:
        resultado = json.loads(requisição.text)["mensagem"]
        print(f"Falha::{resultado}")



for i in range(0,3):
    urlBase = servers[i]
    for l in range(0,6):
        tokenCliente = {"x-api-key": clientes[l]}
        saque(1,30)
        deposito(1,50)
        transferencia(1,2,20)
        saldo(1)
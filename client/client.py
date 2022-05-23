import requests
import json

tokenCliente1 = "6f986d8b-7cd7-4a2b-b645-5791f7b52ea8"
tokenCliente2 = "6a7de581-54d1-4e49-be22-128a00d958b8"
tokenCliente3 = "14457e72-720f-4afa-86a1-08c646aef0fb"
tokenCliente4 = "7ba5640b-3a25-4ecc-9a6e-9c9a129f2cb6"
tokenCliente5 = "29d0de06-6fad-4b8b-bbfe-bba2cc2c6297"
tokenCliente6 = "05281ee0-0bad-4eca-bab1-0fe76f8eb688"

tokens = [tokenCliente1, tokenCliente2, tokenCliente3,
          tokenCliente4, tokenCliente5, tokenCliente6]

serverIp = "http://localhost:"
serverPort1 = "5001/"
serverPort2 = "5002/"
serverPort3 = "5003/"
serverPorts = [serverPort1, serverPort2, serverPort3]

cliente = int(input("Escolha qual cliente vc quer utilizar [1-6]:"))-1
servidor = int(input("Escolha qual servidor vc quer utilizar [1-3]:"))-1

urlBase = serverIp + serverPorts[servidor]
tokenCliente = {"x-api-key": tokens[cliente]}

while True:
    print("--------------------")
    print("Escolha uma opção:")
    print("1-Deposito")
    print("2-Saque")
    print("3-Transferência")
    print("4-Saldo")
    escolha = int(input(":"))

    if (escolha == 1):
        conta = int(input("Escolha a conta desejada [1-10]:"))
        valor = int(input("Escolha o valor do deposito:"))

        requisição = requests.post(
            url=urlBase+"deposito/"+str(conta)+"/"+str(valor), headers=tokenCliente)

        if(requisição.status_code == 200):
            resultado = json.loads(requisição.text)["Saldo"]
            print(f"Sucesso:: Novo saldo da conta {conta}:{resultado}")
        else:
            resultado = json.loads(requisição.text)["mensagem"]
            print(f"Falha::{resultado}")

    if (escolha == 2):
        conta = int(input("Escolha a conta desejada [1-10]:"))
        valor = int(input("Escolha o valor do saque:"))

        requisição = requests.post(
            url=urlBase+"saque/"+str(conta)+"/"+str(valor), headers=tokenCliente)

        if(requisição.status_code == 200):
            resultado = json.loads(requisição.text)["Saldo"]
            print(f"Sucesso:: Novo saldo da conta {conta}:{resultado}")
        else:
            resultado = json.loads(requisição.text)["mensagem"]
            print(f"Falha::{resultado}")

    if (escolha == 3):
        conta1 = int(input("Escolha a conta de origem desejada [1-10]:"))
        conta2 = int(input("Escolha a conta de destino desejada [1-10]:"))
        valor = int(input("Escolha o valor da transferência:"))

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

    if (escolha == 4):
        conta = int(input("Escolha a conta desejada [1-10]:"))

        requisição = requests.get(
            url=urlBase+"saldo/"+str(conta), headers=tokenCliente)

        if(requisição.status_code == 200):
            resultado = json.loads(requisição.text)["Saldo"]
            print(f"Sucesso:: Saldo da conta {conta}:{resultado}")
        else:
            resultado = json.loads(requisição.text)["mensagem"]
            print(f"Falha::{resultado}")

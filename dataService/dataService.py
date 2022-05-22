from datetime import datetime
import conta
from flask import Flask, request
from requestFilter import api_required
import logging

# Inicialização dos dados base para o servidor
tokenServidor1 = "9cdcaba2-2e76-4a34-ae0a-3b3d54e0002d"
tokenServidor2 = "0a8168a8-6b9d-4d0b-9aef-99c5961b9f16"
tokenServidor3 = "854d6b6a-04d4-42d4-a440-8c45eca2f610"

tokens = [tokenServidor1, tokenServidor2, tokenServidor3]

conta1 = conta.Conta(500, 1)
conta2 = conta.Conta(600, 2)
conta3 = conta.Conta(700, 3)
conta4 = conta.Conta(800, 4)
conta5 = conta.Conta(900, 5)
conta6 = conta.Conta(2000, 6)
conta7 = conta.Conta(1000, 7)
conta8 = conta.Conta(1500, 8)
conta9 = conta.Conta(6500, 9)
conta10 = conta.Conta(1600, 10)

contas = [conta1, conta2, conta3, conta4, conta5,
          conta6, conta7, conta8, conta9, conta10]


operacoes = 0


# Configurações do servidor
logging.basicConfig(filename='logs.log', level=logging.DEBUG)
app = Flask(__name__)
app.run(debug=True, port=5000)


# Funções base
def findConta(id_conta):
    for conta in contas:
        if (conta.getId() == id_conta):
            return conta
    print("conta inexistente")
    return -1


# getLock -> verifica se a conta esta travada
# retorna -1 se estiver travada, ou seja se lock == True
# CONTA É OQ:? UM ID, A CONTA JA? PRECISA BUSCAR


def _getLock(id_negoc, conta):
    if(conta._lock):
        print("Conta travada por outro servidor de negocio")
        return -1

# Destrava a conta


def _unLock(id_negoc, conta):
    print("Destravando a conta")
    conta.unLockConta()

# Trava a conta - SO TEM FUNÇÃO PRA DESBLOQUEAR E VERIFICAR O VALOR DA VARIÁVEL, O GET LOCK DEVE TRANCAR?


def _lock(id_negoc, conta):
    print("Travando a conta")
    conta.lockConta()


# Rotas web
@app.route('/<acnt>', methods=['GET'])
@api_required
def getSaldo(acnt):
    global operacoes
    operacoes = operacoes + 1
    id_negocio = tokens.index(request.headers.get("x-api-key")) + 1
    acnt = int(acnt)
    conta = findConta(acnt)

    if(conta == -1):
        return {"mensagem": "Conta não encontrada"}, 404
    logging.info("TIMESTAMP: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S") +
                 " NumOperação: " + str(operacoes) +
                 " ID Servidor Negócio: " + str(id_negocio) +
                 " TipoOperação: " + "getSaldo" +
                 " Conta: " + str(acnt) +
                 " Valor: " + str(conta.getSaldo()))

    return {"Saldo": conta.getSaldo()}, 200


@api_required
@app.route('/<acnt>/<amt>', methods=['POST'])
def setSaldo(id_negoc, id_conta, valor, token):
    conta = findConta(id_conta)

    if(conta == -1):
        return -1

    if (_getLock(id_negoc, conta) == -1):
        return -1

    _lock(id_negoc, conta)

    conta._saldo = valor

    _unLock(id_negoc, conta)

    logging.info("TIMESTAMP: " + datetime.now +
                 " NumOperação: " + operacoes +
                 " ID Servidor Negócio: " + id_negoc +
                 " TipoOperação: " + "setSaldo" +
                 " Conta: " + id_conta +
                 " Valor: " + conta.getSaldo)
    print("valor da conta: ", conta._saldo)

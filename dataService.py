import conta

tokens = ['abadhasj4343nujdas', 'asjdbasdsjkll345678*skad', 'ansjdansjdas-89/*adsa']

conta1  =  conta.Conta(500, 1)
conta2  =  conta.Conta(600, 2)
conta3  =  conta.Conta(700, 3)
conta4  =  conta.Conta(800, 4)
conta5  =  conta.Conta(900, 5)
conta6  =  conta.Conta(2000, 6)
conta7  =  conta.Conta(1000, 7)
conta8  =  conta.Conta(1500, 8)
conta9  =  conta.Conta(6500, 9)
conta10 =  conta.Conta(1600, 10)

contas = [conta1, conta2, conta3, conta4, conta5, conta6, conta7, conta8,conta9, conta10 ]

def tokenIsValid(token):
    if token in tokens:
        return True
    return False

def findConta(id_conta):
    for conta in contas:
        if (conta._id == id_conta ):
            return conta
    print("conta inexistente")
    return -1

## É PASSADO O ID DA CONTA, BUSCADO NO BANCO OU JA É PASSADO DIRETO A CONTA?
def getSaldo(id_negocio, id_conta, token):
    if(not tokenIsValid(token)):
        print("Token invalido")
    
    conta = findConta(id_conta)

    if(conta == -1):
        return -1

    print("valor da conta: ", conta._saldo)

    return conta._saldo

def setSaldo(id_negoc, id_conta, valor, token):
    if(not tokenIsValid(token)):
        print("Token invalido")

    conta = findConta(id_conta)

    if(conta == -1):
        return -1

    if (_getLock(id_negoc, conta) == -1):
        return -1

    _lock(id_negoc, conta)

    conta._saldo = valor

    _unLock(id_negoc, conta)
    
#### getLock -> verifica se a conta esta travada
# retorna -1 se estiver travada, ou seja se lock == True
#CONTA É OQ:? UM ID, A CONTA JA? PRECISA BUSCAR
def _getLock(id_negoc, conta):
    if(conta._lock):
        print("Conta travada por outro servidor de negocio")
        return -1
    
### Destrava a conta
def _unLock(id_negoc, conta):
    print("Destravando a conta")
    conta.unLockConta()

### Trava a conta - SO TEM FUNÇÃO PRA DESBLOQUEAR E VERIFICAR O VALOR DA VARIÁVEL, O GET LOCK DEVE TRANCAR?
def _lock(id_negoc, conta):
    print("Travando a conta")
    conta.lockConta()


import this


class Conta:
    def __init__(self, saldo, id):
        self._id = id
        self._saldo = saldo
        self._lock = False

    def getId(self):
        return self._id

    def getSaldo(self):
        return self._saldo

    def setSaldo(self,novoSaldo):
        self._saldo = novoSaldo

    def isLock(self):
        return self._lock

    def lockConta(self):
        self._lock = True

    def unLockConta(self):
        self._lock = False

class Conta:
    def __init__(self, saldo, id):
        self._id = id
        self._saldo = saldo
        self._lock = False

    def lockConta(self):
        self.lock = True

    def unLockConta(self):
        self.lock = False


class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Olá {self._titular}, seu saldo é de R${self._saldo}'
    
    @property
    def ativar_conta(self):
        return True if self._ativo else False

lucas = ContaBancaria("Lucas", 20)
mariana = ContaBancaria("Mariana", 900)

print(lucas)
print(mariana)
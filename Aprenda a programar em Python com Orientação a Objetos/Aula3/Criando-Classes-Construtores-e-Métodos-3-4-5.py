#Desafio 3, utilizando o codigo do desafio 2, criar o metodo Ativar Conta
class ContaBancaria:
    contas = []

    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        #valor_formatado = "{:,.2f}".format(self.saldo).replace(",", "X").replace(".", ",").replace("X", ".")
        return f'O titular da conta, {self.titular}, possui R$ {self.saldoconta}'

    def ativar_conta(self):
        self._ativo = not self._ativo
        print(f'Conta do Titular {self._titular} foi {self.status}')
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldoconta(self):
        return "{:,.2f}".format(self._saldo).replace(",", "X").replace(".", ",").replace("X", ".")

    @property
    def status(self):
        return 'Ativada' if self._ativo else 'Desativada'
        
conta1 = ContaBancaria('Empresa 1', 160000)
conta2 = ContaBancaria('Pedro', 200)

conta1.ativar_conta()
print(conta1)
print(conta2)
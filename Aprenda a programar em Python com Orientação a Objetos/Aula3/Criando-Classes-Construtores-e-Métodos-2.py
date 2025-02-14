#Desafio 2 - Utilizando o codigo do desafio 1, implementar um metodo __str__
class ContaBancaria:
    contas = []

    def __init__(self, titular='', saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        valor_formatado = "{:,.2f}".format(self.saldo).replace(",", "X").replace(".", ",").replace("X", ".")
        return f'O titular da conta, {self.titular}, possui R$ {valor_formatado}'

conta1 = ContaBancaria('Empresa 1', 160000)
conta2 = ContaBancaria('Pedro', 200)

print(conta1)
print(conta2)
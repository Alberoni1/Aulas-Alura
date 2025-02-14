#Desafio 1
class ContaBancaria:
    contas = []

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
        ContaBancaria.contas.append(self)

    
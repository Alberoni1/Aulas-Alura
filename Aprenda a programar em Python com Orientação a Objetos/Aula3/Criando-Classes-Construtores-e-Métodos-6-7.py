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

class ClienteBanco:
    clientes = []

    def __init__(self,nome, idade, endereco ,cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao
        ClienteBanco.clientes.append(self)

    def __str__(self):
        return f'{self._nome} de {self._idade} anos é cliente no Banco'
    
    @property
    def enderecocliente(self):
        return self._endereco
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular,saldo_inicial)
        return conta

cliente1 = ClienteBanco('João','30', 'Rua 1', '123.456.789.00', 'Autônomo')
conta_cliente1 = ClienteBanco.criar_conta('João', 3000)
print(cliente1)
print(cliente1.enderecocliente)

print(f'A Conta do Titular: {conta_cliente1.titular}\nCom Saldo: {conta_cliente1.saldoconta}\nFoi criada com sucesso!')
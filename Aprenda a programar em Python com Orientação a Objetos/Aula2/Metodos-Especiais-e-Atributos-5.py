class Cliente:
    clientes = []

    def __init__(self, nome, email, numero, idade):
        self.nome = nome
        self.email = email
        self.numero = numero
        self.idade = idade
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.email} | {self.numero} | {self.idade}'

    @classmethod
    def listar_clientes(cls):
        print(f'{"Nome do Cliente".ljust(30)} | {"Email do Cliente".ljust(30)} | {"Telefone do Cliente".ljust(30)} | {"Idade do Cliente"}')
        for cliente in cls.clientes:
            print(f'{cliente.nome.ljust(30)} | {cliente.email.ljust(30)} | {cliente.numero.ljust(30)} | {cliente.idade.ljust(30)}')

cliente1 = Cliente('João','joao@email.com','(21) 99999-0000', '25')
cliente2 = Cliente('Pedro','pedro@email.com','(11) 98888-1111', '31')
cliente3 = Cliente('Ana', 'ana@email.com', '(31) 97777-0000','28')

Cliente.listar_clientes()
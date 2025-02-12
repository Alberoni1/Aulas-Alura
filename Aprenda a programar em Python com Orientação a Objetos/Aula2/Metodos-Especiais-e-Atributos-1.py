class Carro:
    carros = []

    def __init__(self, modelo, cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    
    def __str__(self):
        return f'{self.modelo.ljust(30)} | {self.cor.ljust(30)} | {self.ano}'
    
    @classmethod
    def listar_carros(cls):
        print(f'{"Modelo do Carro".ljust(30)} | {"Cor do Carro".ljust(30)} | {"Ano do Carro"}')
        for carro in cls.carros:
            print(f'{carro.modelo.ljust(30)} | {carro.cor.ljust(30)} | {carro.ano}')

carro_pulse = Carro('Pulse','Prata','2025')
Carro.listar_carros()
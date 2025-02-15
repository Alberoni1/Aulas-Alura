from modelos.veiculos import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo,cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        return f'{self.marca} {self.modelo} Cor: {self.cor} - Estado: {self.ligado}'
    
    def ligar(self):
        return super().ligar()
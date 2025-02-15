from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    ''' Exercicio 2 '''
    def __str__(self):
        return f'{self.marca} {self.modelo} - Estado: {self.ligado}'

    @property
    def ligado(self):
        return 'ligado' if self._ligado else 'desligado'
    
    @abstractmethod
    def ligar(self):
        self._ligado = not self._ligado
        
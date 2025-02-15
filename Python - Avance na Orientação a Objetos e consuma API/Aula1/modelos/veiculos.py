class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    ''' Exercicio 2 '''
    def __str__(self):
        return f'{self.marca} {self.modelo} está {self.ligado}'

    @property
    def ligado(self):
        return 'ligado' if self._ligado else 'desligado'
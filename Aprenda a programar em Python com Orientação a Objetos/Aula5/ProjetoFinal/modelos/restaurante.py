class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(30)} | {"Categoria".ljust(30)} | {"Status".ljust(30)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(30)} | {restaurante.categoria.ljust(30)} | {restaurante.ativo}')

    @classmethod
    def alterar_nome_restaurante(cls):
        pergunta = input('Digite o Restaurante a ter o Nome alterado: ').title()
        for restaurante in cls.restaurantes:
            if pergunta == restaurante.nome:
                nome = input('Insira o novo nome do restaurante: ').title()
                restaurante.nome = nome
    @classmethod
    def alterar_categoria(cls):
        pergunta = input('Digite o Restaurante a ter a Categoria alterada: ').title()
        for restaurante in cls.restaurantes:
            if pergunta == restaurante.nome:
                categoria = input('Insira a nova Categoria do restaurante: ').title()
                restaurante.categoria = categoria
    
    @property
    def ativo(self):
        return 'Aberto' if self._status else 'Fechado'
    
    def alterar_status(self):
        self._status = not self._status





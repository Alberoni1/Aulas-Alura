class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria,ativo,avaliacao,preco):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.preco = preco
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome.ljust(15)} | {self.categoria.ljust(15)} | {self.ativo.ljust(15)} | {self.avaliacao.ljust(15)} | {self.preco} '
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(15)} | {"Status".ljust(15)} | {"Avaliação".ljust(15)} | {"Caro ou Barato"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(15)} | {restaurante.ativo.ljust(15)} | {restaurante.avaliacao.ljust(15)} | {restaurante.preco}')

lugar1 = Restaurante('Sushi', 'Japonesa', 'Ativo', '3.5', 'Médio')

Restaurante.listar_restaurantes()
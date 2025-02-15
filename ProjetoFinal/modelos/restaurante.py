from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.clientes.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self.categoria = categoria
        self._status = False
        self._cardapio = []
        self._avaliacao  = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria} | {self.ativo}'
    
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

    def receber_avaliacao(self,cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)


    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_de_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qnt_notas = len(self._avaliacao)
        media = soma_de_notas/qnt_notas
        return media
    
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapiod do Restaurante{self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            mensagem = f'{i}. Nome:{item._item} | Preço: R${"{:,.2f}".format(item._preco).replace(",", "X").replace(".", ",").replace("X", ".")}'
            print(mensagem)

from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, item, preco,tamanho):
        super().__init__(item, preco)
        self.tamanho = tamanho

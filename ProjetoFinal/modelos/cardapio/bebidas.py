from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, item, preco,tamanho):
        super().__init__(item, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._item
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)

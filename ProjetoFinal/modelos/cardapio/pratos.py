from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, item, preco,descricao):
        super().__init__(item, preco)
        self.descricao = descricao

    def __str__(self):
        return self._item
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
    

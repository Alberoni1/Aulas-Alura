from cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, item, preco,tipo,tamanho,descricao):
        super().__init__(item, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.decricao = descricao
    
    def __str__(self):
        return self._item

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.00)
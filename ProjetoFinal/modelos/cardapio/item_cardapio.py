from abc import ABC, abstractmethod


class ItemCardapio:
    def __init__(self,item,preco):
        self._item = item
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass
    
from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.pratos import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'Grande')
prato_pao = Prato('Pão de Leite', 1.5,'Poção de Pão de Leite')

restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(bebida_suco)

def main():
    restaurante_praca.exibir_cardapio

    

if __name__== '__main__':
    main()
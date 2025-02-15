from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Victor', 9)
restaurante_praca.receber_avaliacao('Amanda', 6)
restaurante_praca.receber_avaliacao('Marcos', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
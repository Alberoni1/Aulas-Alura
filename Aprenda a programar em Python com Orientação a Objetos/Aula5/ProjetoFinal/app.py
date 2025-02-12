from modelos.restaurante import Restaurante
lugar1 = Restaurante('Sushi', 'Japonesa')
def main():
    lugar1.alterar_status()
    Restaurante.listar_restaurantes()

    

if __name__== '__main__':
    main()
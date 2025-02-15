from modelos.carros import Carro


carro1 = Carro('Fiat', 'Pulse', 'Prata')
carro2 = Carro('Chevrolet','Camaro','Amarelo')
carro3 = Carro('Volkswagen', 'Gol', 'Branco')

def main():
    print('')
    print(carro1)
    carro2.ligar()
    print('')
    print(carro2)
    print('')
    print(carro3)
    print('Motorista dando partida')
    carro3.ligar()
    print(carro3)
    print('')

if __name__ == '__main__':
    main()
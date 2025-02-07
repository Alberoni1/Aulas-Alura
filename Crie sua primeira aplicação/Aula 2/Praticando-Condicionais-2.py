idade = int(input('Digite a sua Idade: '))

if idade in range(0,13):
    print(f'Você tem {idade} anos e é uma Criança')
elif idade in range(13, 19):
    print(f'Você tem {idade} anos e é um Adolescente')
else:
    print(f'Você tem {idade} anos e é um Adulto')
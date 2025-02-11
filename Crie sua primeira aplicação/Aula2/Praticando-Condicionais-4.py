print('Informe uma coordenada (X,Y) para saber o seu Quadrante Cartesiano')
x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

coordenada_eixo = f'A coordenada ({x},{y}) esta no Eixo ou na Origem'

if x > 0:
    if y > 0:
        print(f'A coordenada ({x}, {y}) esta no Primeiro Quadrante')
    elif y < 0:
        print(f'A coordenada ({x}, {y}) esta no Quarto Quadrante')
    else:
        print(coordenada_eixo)
elif x < 0:
    if y > 0:
        print(f'A coordenada ({x}, {y}) esta no Segundo Quadrante')
    elif y < 0:
        print(f'A coordenada ({x}, {y}) esta no Terceiro Quadrante')
    else:
        print(coordenada_eixo)
else:
    print(coordenada_eixo)
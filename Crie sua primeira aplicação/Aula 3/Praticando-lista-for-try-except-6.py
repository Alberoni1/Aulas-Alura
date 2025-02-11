lista = [40,32,98,31,25,84,954,36,1,0,45,2]
x = 0
try:
    for i in lista:
        x += i
    print(f'O somatório dos valores contidos na Lista é: {x}')
except:
    print('Lista Invalida')
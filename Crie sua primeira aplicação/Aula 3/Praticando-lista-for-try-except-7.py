lista = [40,32,98,31,25,84,954,36,1,0,45,2]
#lista = []
x = 0
try:
    for i in lista:
            x += i
    y = len(lista)
    media = x/y
    print(f'A média dos valores contidos na Lista é: {media}')
except:
    print('Lista invalida, impossivel divisão por 0')
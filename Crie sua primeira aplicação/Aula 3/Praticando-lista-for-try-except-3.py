#Lista de números de 1 a 10;
lista1 = [1,2,3,4,5,6,7,8,9,10]
x=0

for i in lista1:
    if i % 2 != 0:
        x += i

print(f'A soma dos numeros impares, de 1 a 10, é: {x}')
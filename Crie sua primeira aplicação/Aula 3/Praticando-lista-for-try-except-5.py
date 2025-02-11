print('Para saber a Tabuada')
x = int(input('Digite um Numero: '))
b = 1
for i in range(10):
    y = b*x
    b += 1
    print(f'{b-1} x {x} = {y}')


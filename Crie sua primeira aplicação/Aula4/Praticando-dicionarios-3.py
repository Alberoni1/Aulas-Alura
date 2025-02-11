#lista de dicionarios que representa o numero e seu quadrado
quadrados = [{'numero':'1','quadrado':'1'},{'numero':'2','quadrado':'4'},{'numero':'3','quadrado':'9'},{'numero':'4','quadrado':'16'},{'numero':'5','quadrado':'25'}]

quadrados_calculados = []

for i in range(5):
    x = i+1
    x_2 = x**(2)
    dicionario = {'numero':str(x),'quadrado':str(x_2)}
    quadrados_calculados.append(dicionario)

print('Imprimindo lista Pré-definida')
print(f'{'Numero'.ljust(20)} | {'Quadrado'}')
for quadrado in quadrados:
    numero = quadrado['numero']
    quad = quadrado['quadrado']
    print(f'{numero.ljust(20)} | {quad}')

print('\nImprimindo lista Calculada\n')
print(f'{'Numero'.ljust(20)} | {'Quadrado'}')
for quadrado in quadrados_calculados:
    numero = quadrado['numero']
    quad = quadrado['quadrado']
    print(f'{numero.ljust(20)} | {quad}')
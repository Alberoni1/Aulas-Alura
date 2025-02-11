frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."

contar_palavra = {}
palavras = frase.split()
for palavra in palavras:
    contar_palavra[palavra] = contar_palavra.get(palavra, 0) + 1
print(contar_palavra)
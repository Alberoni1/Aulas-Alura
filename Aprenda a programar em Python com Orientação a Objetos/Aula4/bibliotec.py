from exercicios import Livro

livro1 = Livro('As Crônicas de Nárnia','C.S. Lewis', 1950)
livro2 = Livro('As Crônicas de Gelo e Fogo', 'George R. R. Martin', 1996)
livro3 = Livro('Python Cookbook', 'Samuel Developer', 2019)
livro4 = Livro('Aprendendo Python', 'John Doe', 2022)
livro5 = Livro('Data Science Fundamentals', 'Jane Smith', 2020)
livro6 = Livro('À Espera de um Milagre', 'Stephen King', 1996)

print(livro2.disponivel())

for livro in Livro.verificar_disponibilidade(1996):
    print(livro)
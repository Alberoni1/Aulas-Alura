import os
class Musicas:
    musica = []
    def __init__(self,nome,artista,duracao):
        self.nome = nome.title()
        self.artista = artista.title()
        self.duracao = duracao
        Musicas.musica.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    @classmethod
    def listar_musicas(cls):
        print(f'{"Nome da Musica".ljust(30)} | {"Nome do Artista".ljust(30)} | {"Duração".ljust(30)}')
        for musica in cls.musica:
            print(f'{musica.nome.ljust(30)} | {musica.artista.ljust(30)} | {musica.duracao.ljust(30)}')

    @classmethod
    def cadastrar_musica(cls):
        cls.nome = input('Digite o nome da Musica: ')
        cls.artista = input('Insira o Artista da Musica: ')
        cls.duracao = input('Insira a duração da musica: ')

        Musicas(cls.nome,cls.artista,cls.duracao)


Musicas.cadastrar_musica()
os.system('cls')
Musicas.listar_musicas()
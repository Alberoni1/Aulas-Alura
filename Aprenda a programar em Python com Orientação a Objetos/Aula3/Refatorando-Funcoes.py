class Pessoa:
    pessoas = []

    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome} tem {str(self.idade)} e trabalha com {self.profissao}'
      
    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        if self.profissao:
            return f'Olá!! sou {self.nome}! Eu trabalho com {self.profissao}'
        else:
            return f'Olá! me chamo {self.nome}'

pessoa1 = Pessoa('João',29,'Engenharia')

print(pessoa1.saudacao())
pessoa1.aniversario()
print(pessoa1)
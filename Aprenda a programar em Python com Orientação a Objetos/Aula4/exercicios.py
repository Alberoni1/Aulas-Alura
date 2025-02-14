class Livro:
    livros = []

    def __init__(self,titulo,autor,ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Livro: "{self._titulo}" de {self._autor} publicado em {str(self._ano_publicado)}'

    def emprestar(self):
        self._disponivel = False
        return 'Livro emprestado'

    def disponivel(self):
        return f'Livro "{self._titulo}" está Disponível' if self._disponivel else f'Livro "{self._titulo}" está Indisponível'    

    @staticmethod
    def verificar_disponibilidade(ano):
        print(f'Livros publicados em {ano} disponiveis')
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicado == ano and livro._disponivel]
        return livros_disponiveis
    
    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'Livro: "{livro._titulo}" de {livro._autor} publicado em {str(livro._ano_publicado)}')
class Restaurante:
    restaurantes = []  # Lista compartilhada entre todas as instâncias

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._status = False  # Status inicial é inativo
        Restaurante.restaurantes.append(self)  # Adiciona o restaurante à lista

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'  # Usa a propriedade ativo
    
    @classmethod
    def listar_restaurantes(cls):
        """Lista todos os restaurantes cadastrados na classe."""
        if not cls.restaurantes:
            print("Nenhum restaurante cadastrado.")
            return
        
        print(f'{"Nome do Restaurante".ljust(30)} | {"Categoria".ljust(30)} | {"Status".ljust(30)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(30)} | {restaurante.categoria.ljust(30)} | {restaurante.ativo}')

    @classmethod
    def alterar_nome_restaurante(cls):
        """Permite alterar o nome de um restaurante."""
        pergunta = input('Digite o nome do restaurante a ser alterado: ').title()
        for restaurante in cls.restaurantes:
            if pergunta == restaurante.nome:
                novo_nome = input('Insira o novo nome do restaurante: ').title()
                restaurante.nome = novo_nome
                print(f"Nome alterado para: {novo_nome}")
                return
        print("Restaurante não encontrado.")

    @classmethod
    def alterar_categoria(cls):
        """Permite alterar a categoria de um restaurante."""
        pergunta = input('Digite o nome do restaurante para mudar a categoria: ').title()
        for restaurante in cls.restaurantes:
            if pergunta == restaurante.nome:
                nova_categoria = input('Insira a nova categoria: ').title()
                restaurante.categoria = nova_categoria
                print(f"Categoria alterada para: {nova_categoria}")
                return
        print("Restaurante não encontrado.")

    @property
    def ativo(self):
        """Retorna uma string representando o status do restaurante."""
        return 'Ativo' if self._status else 'Inativo'
    
    def alterar_status(self):
        """Alterna o status do restaurante entre Ativo/Inativo."""
        self._status = not self._status
        print(f"Status alterado para: {self.ativo}")

# Criando um restaurante
lugar1 = Restaurante('Sushi', 'Japonesa')

# Listando os restaurantes para verificar se o cadastro foi feito corretamente
Restaurante.listar_restaurantes()

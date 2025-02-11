import os

#Restaurantes Pré Cadastrados no programa
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

#1. Crie uma docstring para a função exibir_nome_do_programa()
def exibir_nome_do_programa(): #Exibe o Nome do Programa
    
    '''Cria o Nome do Aplicativo'''

    print(""" 
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███████░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░█████████░░░░░░█████████
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ \n""")

#2. Crie uma docstring para a função exibir_opcoes()
def exibir_opcoes(): #Define o Menu Inicial
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurantes')
    print('4. Alterar dados de um Restaurante')
    print('5. Sair\n')

#3. Crie uma docstring para a função finalizar_app()
def finalizar_app(): #Finaliza o App
    exibir_subtitulo('Fechando o App')
    
#4. Crie uma docstring para a função opcao_invalida()
def opcao_invalida(): #Define a função de Opção Invalida
    print('Opção inválida!\n')
    voltar_menu_inicial()

#5. Crie uma docstring para a função exibir_subtitulo(texto)
def exibir_subtitulo(texto): #Define a função de Preparar a Tela, limpando-a, e informando o estagio em que se enconta o App 
    os.system('cls')
    linha = '*'*(len(texto))
    print(linha +'\n')
    print(texto + '\n')
    print(linha +'\n')

#6. Crie uma docstring para a função cadastrar_novo_restaurante()
def cadastrar_novo_restaurante(): #Cadastra o Restaurante Criado
    criar_restaurante()
    opcao = input('Deseja Continuar inserindo Restaurantes? Digite "sim" para Continuar.\nPara Sair pressione "Enter": ').lower()
    if opcao == 'sim':
        while opcao == 'sim':
            criar_restaurante()
            opcao = input('Deseja Continuar inserindo Restaurantes? Digite "sim" para Continuar.\nPara Sair pressione "Enter": ').lower()           
    main()

#7. Crie uma docstring para a função listar_restaurantes()
def listar_restaurantes(): #Lista os Restaurantes Cadastrados
    exibir_subtitulo('  Listando restaurantes  ')
    print(f'{'  Nome do Restaurante'.ljust(27)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(25)} | {categoria.ljust(25)} | {ativo}')
    
    voltar_menu_inicial()

#8. Crie uma docstring para a função alternar_estado_restaurante()
def alternar_estado_restaurante(): #Altera o Status dos Restaurantes Cadastrados
    exibir_subtitulo('  Alterando o Status de um restaurante  ')
    nome_restaurante = input('Digite o nome do restaurante a ser alterado: ').capitalize()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        nome_corrigido = restaurante['nome']
        if nome_restaurante == nome_corrigido.capitalize():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu_inicial()

#9. Crie uma docstring para a função escolher_opcao()
def escolher_opcao(): #Define a função de escolher as opções do Menu Inicial
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()()
        elif opcao_escolhida == 5: 
            finalizar_app()
        elif opcao_escolhida == 4:
            alterar_dados_restaurante()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

#10. Crie uma docstring para a função main()
def main(): #Função Primária
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
  
#11. Criando uma docstring para a função voltar_menu_inicial():
def voltar_menu_inicial():
    input ('\nDigite uma tecla para voltar ao menu principal.')
    main()

#12. Criando uma docstring para a função criar_restaurante()
def criar_restaurante(): #Define uma função para criar o restaurante
    exibir_subtitulo('  Cadastro de Novos Restaurantes  ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ').title()
    if nome_do_restaurante != "":
        categoria_restaurante = input(f'Digite a categoria do restaurante "{nome_do_restaurante}": ').title()
        dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
        restaurantes.append(dados_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    else:
        print('Não é possivel inserir um Restaurante sem Nome,\n Por favor, refaça.')

#13. Criando uma docstring para a Função alterar_dados_restaurante()
def alterar_dados_restaurante(): #Define função para fazer alterações em Restaurantes já cadastrados
    exibir_subtitulo('  Alterando o Informações de um restaurante  ')
    nome_restaurante = input('Digite o nome do restaurante a ser alterado: ').title()
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        nome_corrigido = restaurante['nome']
        if nome_restaurante == nome_corrigido.title():
            restaurante_encontrado = True
            pergunta = input('Qual informação do restaurante você quer mudar? ').lower()
            if pergunta == 'nome':
                nome_antigo = restaurante['nome']
                novo_nome = input('Qual o novo nome do Restaurante? ').title()
                restaurante['nome'] = novo_nome
                mensagem = f'O restaurante "{nome_antigo}" teve seu nome alterado com sucesso, passando a ser "{novo_nome}"'
                print(mensagem)
            elif pergunta == 'categoria':
                categoria_antiga = restaurante['categoria']
                nova_categoria = input('Qual a nova categoria do Restaurante? ').title()
                restaurante['categoria'] = nova_categoria
                mensagem = f'O restaurante "{nome_restaurante}" teve sua categoria alterada com sucesso, passando a ser "{nova_categoria}", antes sendo "{categoria_antiga}"'
                print(mensagem)
            else:
                print('Porfavor Tente Novamente')
                voltar_menu_inicial()
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu_inicial()



if __name__ == '__main__':
    main()
login = input('Digite o seu Usuario: ')
senha = input('Digite a sua Senha: ')

login_salvo = 'testando'
senha_salva = 'Lobinho'

if login == login_salvo:
    if senha == senha_salva:
        print('Você está conectado')
    else:
        print('Senha Incorreta')
else:
    print('Usuário não Cadastrado')
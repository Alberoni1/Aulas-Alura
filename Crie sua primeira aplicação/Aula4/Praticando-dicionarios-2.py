dicionario = [{'Nome':'Victor','Idade':'29','Cidade':'Rio de Janeiro'}]
nome_pessoa = input('Digite o nome da pessoa a ter os dados alterados: ').title()
for pessoa in dicionario:
    nome_corrigido = pessoa['Nome']
    if nome_pessoa == nome_corrigido.title():
        pergunta = input(f'Qual a informação da pessoa {nome_pessoa} você quer alterar: ').capitalize()
        if pergunta == 'Nome':
            nome_antigo = pessoa['Nome']
            novo_nome = input(f'Qual o nome corrigido de {nome_corrigido}: ').title()
            pessoa['Nome'] = novo_nome
            mensagem = f'A pessoa "{nome_antigo}" teve seu nome alterado com sucesso, passando a ser "{novo_nome}"'
            print(mensagem)
        elif pergunta == 'Idade':
            idade_antiga = pessoa['Idade']
            nova_idade = input(f'Qual a idade corrigida de {nome_corrigido}: ')
            pessoa['Idade'] = nova_idade
            mensagem = f'A pessoa "{nome_pessoa}" teve sua idade alterada com sucesso, passando a ter "{nova_idade}"'
            print(mensagem)
        elif pergunta == 'Cidade':
            cidade_antiga = pessoa['Cidade']
            nova_cidade = input(f'Qual a Cidade corrigida de {nome_corrigido}: ').title()
            pessoa['Cidade'] = nova_cidade
            mensagem = f'A pessoa "{nome_pessoa}" teve sua Cidade alterada com sucesso, passando a ser "{nova_cidade}"'
            print(mensagem)
        
        else:
            print(f'Pessoa {nome_pessoa} não encontrada, tente novamente')
print(f'{' - Nome da Pessoa'.ljust(23)} | {'Idade'.ljust(20)} | {'Cidade'.ljust(20)}\n')
for pessoa in dicionario:
    nome_pessoa = pessoa['Nome']
    cidade_pessoa = pessoa['Cidade']
    idade_pessoa = pessoa['Idade']

    print(f' - {nome_pessoa.ljust(20)} | {idade_pessoa.ljust(20)} | {cidade_pessoa.ljust(20)}')
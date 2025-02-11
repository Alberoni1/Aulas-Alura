quadrados = {'numero':'1','quadrado':'1'}

pesquisa = input('Qual item você quer verificar se existe no dicionario: ')
if pesquisa in quadrados:
    print(f'O item "{pesquisa}" existe no Dicionario')
else:
    print(f'O item "{pesquisa}" NÃO existe no Dicionario')
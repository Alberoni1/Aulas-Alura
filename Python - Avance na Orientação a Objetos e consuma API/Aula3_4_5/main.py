from fastapi import FastAPI,Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    ''' Endpoint do Hello World '''
    
    return {'Hello':'World'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurantes: str = Query(None)):
    ''' Endpoint para ver os cardápios dos Restaurantes '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_jason = response.json()
        if restaurantes is None:
            return{'Dados':dados_jason}
        
        dados_restaurante = []
        for item in dados_jason:
            if item['Company'] == restaurantes:         
                dados_restaurante.append({
                    'item':item['Item'],
                    'price':item['price'],
                    'description':item['description']
                })
        return {'Restaurante':restaurantes,'Cardapio':dados_restaurante}
    else:
        return{'Erro':f'{response.status_code} - {response.text}'}
from calculadora_media_consumo import ContaCliente
import math

class CalculoSolar:
    def __init__(self,desempenho,cliente):
        self.irradiacao = []
        self.desempenho = desempenho
        self.cliente = cliente
        self.lista_ger_esperada = []

    def __str__(self):
        return f"Calculo Solar para {self.cliente.cliente}"

    @property 
    def calculo_solar(self):
        consumo_medio = int(self.cliente.media_consumo)
        pger = round((consumo_medio*1)/(30*float(self.media_irradiacao)*self.desempenho),2)
        return pger
    
    def paineis_sistema(self):
        pger = int(self.calculo_solar)
        pot_painel = int(input('Digite a potencia do Painel: '))
        qnt_painel = math.ceil(pger/(pot_painel/1000))
        return qnt_painel
    
    def recebe_irradiacao(self):
        for mes in ContaCliente.meses:
            irradiacao_mes = float(input(f'Digite a irradiação para {mes}: '))
            self.irradiacao.append(irradiacao_mes)
    
    @property
    def media_irradiacao(self):
        if not self.irradiacao:
            return 0
        soma_irradiacao = sum(self.irradiacao)
        print(soma_irradiacao)
        qnt_meses = len(self.irradiacao)      
        media = round(soma_irradiacao/qnt_meses,2)
        return media

    @property
    def calc_geracao_esperada(self):
 
        for a,b in zip(self.cliente._consumo, self.irradiacao):
            geracao_esp = a*b
            self.lista_ger_esperada.append(geracao_esp)

    def lista_geracao_esperada(self):
        resultados =[]
        for a,b in zip(self.lista_ger_esperada,self.cliente.meses):
            resultados.append(f'Mês: {b} | Geração Esperada: {a}')
        return resultados



    
casa = ContaCliente('Casa')
casa.recebe_consumo()
modelo = CalculoSolar(0.7,casa)
modelo.recebe_irradiacao()
print(modelo.calculo_solar)
print(modelo.paineis_sistema())
modelo.calc_geracao_esperada
print(modelo.lista_geracao_esperada())

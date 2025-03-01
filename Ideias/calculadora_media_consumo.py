from adicao_potencia import AdicionaPotencia

class ContaCliente:
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    def __init__(self,cliente):
        self.cliente = cliente
        self._consumo = []

    def __str__(self):
        return f'Cliente: {self.cliente}'
    
    def recebe_consumo(self):
        for mes in ContaCliente.meses:
            consumo_mes = float(input(f'Consumo para o mês {mes}: '))
            self._consumo.append(consumo_mes)

    @property
    def media_consumo(self):
        if not self._consumo:
            return 0
        soma_consumo = sum(self._consumo)
        qtd_meses = len(self._consumo)
        media = round(soma_consumo/qtd_meses, 2)
        return media

    
# criar uma função de adição de carga 
# CONSUMO (kWh) = potência (W) x horas de uso por dia (h) x dias de uso no mês / 1000.


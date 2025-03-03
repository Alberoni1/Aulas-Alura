from django.db import models
from django.forms import ValidationError
from clientes.models import ClientePJ
from calculosolar.models import CalculoIrradianciaSolar,AdicaoPotenciaKWHMes,CalcPotenciaAdicional
import math

class CalculoSolarPJ(models.Model):
    cliente = models.ForeignKey(ClientePJ, on_delete=models.CASCADE)
    cons_jan = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Janeiro',null=False,blank=False)
    cons_fev = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Fevereiro',null=False,blank=False)
    cons_mar = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Março',null=False,blank=False)
    cons_abr = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Abril',null=False,blank=False)
    cons_mai = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Maio',null=False,blank=False)
    cons_jun = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Junho',null=False,blank=False)
    cons_jul = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Julho',null=False,blank=False)
    cons_ago = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Agosto',null=False,blank=False)
    cons_set = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Setembro',null=False,blank=False)
    cons_out = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Outubro',null=False,blank=False)
    cons_nov = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Novembro',null=False,blank=False)
    cons_dez = models.IntegerField(default=0,verbose_name='Irradiancia (kWh) Dezembro',null=False,blank=False)

    @property
    def media_consumo(self):
        meses = [
            self.cons_jan,self.cons_fev,self.cons_mar,
            self.cons_abr,self.cons_mai,self.cons_jun,
            self.cons_jul,self.cons_ago,self.cons_set,
            self.cons_out,self.cons_nov,self.cons_dez
        ]
        return sum(meses)/12 if all(meses) else 0

    def clean(self):
        if any(valor < 0 for valor in [
            self.cons_jan, self.cons_fev, self.cons_mar,
            self.cons_abr, self.cons_mai, self.cons_jun,
            self.cons_jul, self.cons_ago, self.cons_set,
            self.cons_out, self.cons_nov, self.cons_dez
        ]):
            raise ValidationError("Os valores de consumo não podem ser negativos")
        
    def __str__(self):
        return f'Media de consumo para {self.cliente.nome} - Média: {self.media_consumo:.2f} kWh/mês'

    class Meta:
        verbose_name = 'Consumo Médio PJ'
        verbose_name_plural = 'Consumos Médios PJs'
        ordering = ['-id']

class CalculoPotenciaGeracaoPJ(models.Model):
    cliente = models.ForeignKey(ClientePJ, on_delete=models.CASCADE)
    consumo = models.ForeignKey(CalculoSolarPJ,on_delete=models.CASCADE)
#    adicconsumo = models.ForeignKey(AdicaoPotenciaKWHMes,on_delete=models.CASCADE,verbose_name='Consumo Adicional')
    irradi = models.ForeignKey(CalculoIrradianciaSolar,on_delete=models.CASCADE,verbose_name='Irradiação Solar')
    rendimento = models.IntegerField(default=100,null=False,blank=False,verbose_name='Rendimento do Sistema %')
    
    @property
    def calculogeracao(self):
        #pger = ((self.consumo.media_consumo) + (self.adicconsumo))*1/(30*(self.irradi.media_irradiacao)) qndo fizer a classe de Adicional de consumo
        pger = (self.consumo.media_consumo)*1/(30*(self.irradi.media_irradiancia)*(self.rendimento/100))
        return pger
    
    def __str__(self):
        return f'Potencia do Sistema: {self.calculogeracao} kWp'
    
    class Meta:
        verbose_name = 'Potência de Geração Necessária PJ'
        verbose_name_plural = 'Potências de Geração Necessárias PJs'
        ordering = ['-id']

class QntPaineisPJ(models.Model):
    cliente = models.ForeignKey(ClientePJ, on_delete=models.CASCADE,default=0)
    potgeracao = models.ForeignKey(CalculoPotenciaGeracaoPJ, on_delete=models.CASCADE,verbose_name='Potência de Geração',default=0)
    potpainel = models.IntegerField(default=0,null=False,blank=False,verbose_name='Potencia do Painel (W)')

    @property
    def calculopainel(self):
        n_painel = math.ceil(self.potgeracao.calculogeracao/(self.potpainel/1000))
        return n_painel
    
    @property
    def potenciasistema(self):
        potsis = self.calculopainel*(self.potpainel/1000)
        return potsis

    def __str__(self):
        return f'Numero de Paineis necessarios: {self.calculopainel}'

    class Meta:
        verbose_name = 'Quantdade de Painel Necessário PJ'
        verbose_name_plural = 'Quantdade de Paineis Necessários PJs'
        ordering = ['-id']

class AdicaoPotenciaKWHMes(models.Model): #adiciona a potencia ao consumo médio
    pass

class CalcPotenciaAdicional(models.Model): # Faz o calculo de Consumo do Aparelho a Partir da Potencia
    pass

class GeracaoPrevistaPJ(models.Model):
    cliente = models.ForeignKey(ClientePJ, on_delete=models.CASCADE)
    potsist = models.ForeignKey(QntPaineisPJ, on_delete=models.CASCADE,verbose_name='Potencia do Sistema')
    irrad = models.ForeignKey(CalculoIrradianciaSolar, on_delete=models.CASCADE,verbose_name='Irradiância Local')
    rend = models.ForeignKey(CalculoPotenciaGeracaoPJ, on_delete=models.CASCADE, verbose_name='Rendimento')
    
    @property
    def gercaoesperada(self):
        
        irradiancias = [
            float(self.irrad.irradi_jan),float(self.irrad.irradi_fev),float(self.irrad.irradi_mar),
            float(self.irrad.irradi_abr),float(self.irrad.irradi_mai),float(self.irrad.irradi_jun),
            float(self.irrad.irradi_jul),float(self.irrad.irradi_ago),float(self.irrad.irradi_set),
            float(self.irrad.irradi_out),float(self.irrad.irradi_nov),float(self.irrad.irradi_dez),
        ]

        dias_no_mes = [
            31, 28, 31,
            30, 31, 30, 
            31, 31, 30, 
            31, 30, 31
            ]

        meses = [
            'Janeiro','Fevereiro','Março',
            'Abril','Maio','Junho',
            'Julho','Agosto','Setembro',
            'Outubro','Novembro','Dezembro'
        ]

        geracao_mensal = []

        for mes,irradiancia,dia in zip(meses, irradiancias, dias_no_mes):
            pot_sistema = float(self.potsist.potenciasistema)
            rendimento = float(self.rend.rendimento)            
            geracao = (irradiancia*dia*pot_sistema*rendimento)/100
            geracao_mensal.append((mes,geracao))

        return geracao_mensal
    
    def __str__(self):
        return f"Geracao Prevista para {self.cliente}"

    @property
    def rendimento_do_sistema(self):
        return self.rend.rendimento  # Acessa o rendimento diretamente

    @property
    def irradiacao_media(self):
        return self.rend.irradi.media_irradiancia
   
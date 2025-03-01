from django.db import models
from django.forms import ValidationError
from clientes.models import ClientePF,ClientePJ



class CalculoSolarPF(models.Model):
    cliente = models.ForeignKey(ClientePF, on_delete=models.CASCADE)
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
        verbose_name = 'Consumo Médio PF'
        verbose_name_plural = 'Consumos Médios PFs'
        ordering = ['-id']



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

class CalculoIrradianciaSolar(models.Model):
    estado = models.CharField(default='',max_length=200,null=False,blank=False)
    cidade = models.CharField(default='',max_length=200,null=False,blank=False)
    bairro = models.CharField(default='',max_length=200,null=False,blank=False)
    irradi_jan = models.FloatField(default=0,verbose_name='Irradiancia Janeiro',null=False,blank=False)
    irradi_fev = models.FloatField(default=0,verbose_name='Irradiancia Fevereiro',null=False,blank=False)
    irradi_mar = models.FloatField(default=0,verbose_name='Irradiancia Março',null=False,blank=False)
    irradi_abr = models.FloatField(default=0,verbose_name='Irradiancia Abril',null=False,blank=False)
    irradi_mai = models.FloatField(default=0,verbose_name='Irradiancia Maio',null=False,blank=False)
    irradi_jun = models.FloatField(default=0,verbose_name='Irradiancia Junho',null=False,blank=False)
    irradi_jul = models.FloatField(default=0,verbose_name='Irradiancia Julho',null=False,blank=False)
    irradi_ago = models.FloatField(default=0,verbose_name='Irradiancia Agosto',null=False,blank=False)
    irradi_set = models.FloatField(default=0,verbose_name='Irradiancia Setembro',null=False,blank=False)
    irradi_out = models.FloatField(default=0,verbose_name='Irradiancia Outubro',null=False,blank=False)
    irradi_nov = models.FloatField(default=0,verbose_name='Irradiancia Novembro',null=False,blank=False)
    irradi_dez = models.FloatField(default=0,verbose_name='Irradiancia Dezembro',null=False,blank=False)

    @property
    def media_irradiancia(self):
        meses = [
            self.irradi_jan,self.irradi_fev,self.irradi_mar,
            self.irradi_abr,self.irradi_mai,self.irradi_jun,
            self.irradi_jul,self.irradi_ago,self.irradi_set,
            self.irradi_out,self.irradi_nov,self.irradi_dez
        ]
        return sum(meses)/12 if all(meses) else 0

    def clean(self):
        if any(valor < 0 for valor in [
            self.irradi_jan, self.irradi_fev, self.irradi_mar,
            self.irradi_abr, self.irradi_mai, self.irradi_jun,
            self.irradi_jul, self.irradi_ago, self.irradi_set,
            self.irradi_out, self.irradi_nov, self.irradi_dez
        ]):
            raise ValidationError("Os valores de Irradiancia não podem ser negativos")
        
    def __str__(self):
        return f'Irradiancia Média: {self.media_irradiancia:.2f} kWh/m^(2).dia'

    class Meta:
        verbose_name = 'Irradiancia Média'
        verbose_name_plural = 'Irradiancias Médias'
        ordering = ['-id']

class AdicaoPotenciaKWHMes(models.Model): #adiciona a potencia ao consumo médio
    pass

class CalcPotenciaAdicional(models.Model): # Faz o calculo de Consumo do Aparelho a Partir da Potencia
    pass

class CalculoPotenciaGeracaoPF(models.Model):
    cliente = models.ForeignKey(ClientePF, on_delete=models.CASCADE)
    consumo = models.ForeignKey(CalculoSolarPF,on_delete=models.CASCADE)
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
        verbose_name = 'Potência de Geração Necessária PF'
        verbose_name_plural = 'Potências de Geração Necessárias PFs'
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

class QntPaineisPF(models.Model):
    pass

class QntPaineisPJ(models.Model):
    pass
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
        verbose_name = 'Cálculo Consumo Médio'
        verbose_name_plural = 'Cálculos Consumos Médios'
        ordering = ['-id']

class CalculoIrradianciaSolar(models.Model):
    cliente = models.ForeignKey(ClientePF, on_delete=models.CASCADE)
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
        return f'Media de Irradiancia para {self.cliente.nome} - Média: {self.media_irradiancia:.2f} kWh/m^(2).dia'

    class Meta:
        verbose_name = 'Cálculo Irradiancia Média'
        verbose_name_plural = 'Cálculos Irradiancias Médias'
        ordering = ['-id']
from django.db import models
from datetime import datetime
from smart_selects.db_fields import ChainedForeignKey


class Categoria(models.Model):
    nome = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='tipos')

    def __str__(self):
        return f"{self.nome} ({self.categoria.nome})"

class Veiculos(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
    )

    tipo = ChainedForeignKey(
        Tipo,
        chained_field="categoria",        
        chained_model_field="categoria",  
        show_all=False,
        auto_choose=True,
        sort=True,
        # Importante para evitar erro ao adicionar em tabela com dados existentes:
        null=True,       # permite nulo
        blank=True

    )


        
    caracteristica = models.CharField(max_length=200, null=True, blank=True)

    marca = models.CharField(max_length=100, null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)

    n_rodas = models.IntegerField(null=False,blank=False)
    n_portas = models.IntegerField(null=False,blank=False)
    n_passageiros = models.IntegerField(null=False,blank=False)

    disponivel = models.BooleanField(default=True)
    ligado = models.BooleanField(default=True)
    placa = models.CharField(max_length=9, null=False,blank=False)

    foto_carro = models.ImageField(upload_to='veiculos/%Y/%m/%d/', blank=True)
    data_publicado = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"
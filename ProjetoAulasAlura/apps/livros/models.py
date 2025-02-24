from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):

    titulo = models.CharField(max_length=100,blank=False,null=False)
    paginas = models.IntegerField(blank=False,null=False)
    capa = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    sinopse = models.TextField(max_length=2000)
    categorias = models.ManyToManyField(Categoria)
    disponivel = models.BooleanField(default=True)
    editora = models.CharField(max_length=100,null=False, blank=False)
    autor = models.CharField(max_length=100,null=False, blank=False)
    data_cadastro = models.DateTimeField(default=datetime.now)
    data_emprestado = models.DateTimeField(default=datetime.now,blank=True,null=True)
    data_devolucao  = models.DateTimeField(default=datetime.now,blank=True,null=True)
    ano_publicado = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.titulo
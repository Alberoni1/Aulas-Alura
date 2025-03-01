from django.contrib import admin
from apps.veiculos.models import Veiculos,Categoria,Tipo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')
    search_fields = ('nome', 'categoria__nome')
    list_per_page = 15

@admin.register(Veiculos)
class ListandoVeiculos(admin.ModelAdmin):
    list_display = ('id', 'placa', 'marca', 'modelo', 'categoria', 'tipo', 'disponivel')
    list_display_links = ('id','marca','modelo')
    search_fields = ('placa', 'marca', 'modelo')
    list_filter = ('categoria', 'tipo', 'disponivel')
    list_editable = ('disponivel',)
    list_per_page = 15


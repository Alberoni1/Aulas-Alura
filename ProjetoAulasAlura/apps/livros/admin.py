from django.contrib import admin
from apps.livros.models import Livro,Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class ListandoLivros(admin.ModelAdmin):
    list_display=('id','titulo','autor','editora','ano_publicado','data_cadastro','disponivel',)
    list_display_links=('id','titulo',)
    search_fields=('titulo',)
    list_filter=('autor',)
    list_editable=('disponivel',)
    list_per_page=10
    filter_horizontal = ('categorias',)
    

admin.site.register(Livro,ListandoLivros)

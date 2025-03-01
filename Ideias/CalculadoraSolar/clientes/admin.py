from django.contrib import admin
from clientes.models import ClientePF,ClientePJ,ContaClientePFFile,ContaClientePJFile

class ContaClientePFFileInline(admin.TabularInline):
    model = ContaClientePFFile
    extra = 1

class ContaClientePJFileInline(admin.TabularInline):
    model = ContaClientePJFile
    extra = 1


@admin.register(ClientePF)
class ClientePFAdmin(admin.ModelAdmin):
    list_display=('id','nome','email','cpf','celular','data_nascimento')
    list_display_links=('id','nome',)
    list_per_page=20
    search_fields=('nome',)
    inlines = [ContaClientePFFileInline]

@admin.register(ClientePJ)
class ClientePJAdmin(admin.ModelAdmin):
    list_display=('id','nome','email','cnpj','celular',)
    list_display_links=('id','nome',)
    list_per_page=20
    search_fields=('nome',)
    inlines = [ContaClientePJFileInline]

    



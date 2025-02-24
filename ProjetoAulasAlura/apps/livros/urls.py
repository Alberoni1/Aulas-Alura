from django.urls import path
from apps.livros.views import index,livros,livro,filtro,alugar,devolver

urlpatterns = [
    path('',index,name='index'),
    path('livros/',livros,name='livros'),
    path('livros/<int:livro_id>/',livro,name='livro'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    path('alugar/<int:livro_id>',alugar,name='alugar'),
    path('devolver/<int:livro_id>',devolver,name='devolver'),
]
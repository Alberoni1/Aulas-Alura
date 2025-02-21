from django.urls import path
from apps.galeria.views import index,imagem,buscar,upload_foto,remover_foto,edit_foto, filtro

urlpatterns = [
    path('', index, name= 'index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar ,name= 'buscar'),
    path('upload',upload_foto, name='upload_foto'),
    path('edit-foto/<int:foto_id>',edit_foto, name='edit_foto'),
    path('remover-foto/<int:foto_id>', remover_foto, name='remover_foto'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]
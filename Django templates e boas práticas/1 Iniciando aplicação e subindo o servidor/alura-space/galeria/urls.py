from django.urls import path
from galeria.views import index,imagem,buscar,upload_foto

urlpatterns = [
    path('', index, name= 'index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar ,name= 'buscar'),
    path('upload',upload_foto, name='upload_foto')
]
from django.shortcuts import render, get_object_or_404,redirect
from apps.livros.models import Livro, Categoria
from datetime import datetime

def index(request):
    return render(request,'index.html')

def livros(request):
    categorias = Categoria.objects.filter(livro__isnull=False).distinct().order_by('nome')
    livros_disponiveis = Livro.objects.order_by('titulo')
    return render(request, 'livros/livros-index.html', {'cards': livros_disponiveis, 'categorias': categorias})

def livro(request, livro_id):
    livro = get_object_or_404(Livro,pk=livro_id)
    return render(request,'livros/livro.html',{'livros':livro})

def filtro(request, categoria):
    # Busca a categoria pelo nome
    categoria_obj = get_object_or_404(Categoria, nome=categoria)
    # Filtra livros pela categoria (ajuste o nome do campo se necessário)
    livros = Livro.objects.filter(categorias=categoria_obj).order_by('titulo')
    return render(request, 'livros/livros-index.html', {'cards': livros, 'categorias': Categoria.objects.all()})

def alugar(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        if livro.disponivel:
            livro.disponivel = False
            livro.data_emprestado = datetime.now()
            livro.save()
        return redirect('livro', livro_id=livro.id)  # Redirecione para uma view adequada
    return redirect('livros')  # Caso não seja POST

def devolver(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        if not livro.disponivel:
            livro.disponivel = True
            livro.data_devolucao = datetime.now()
            livro.save()
        return redirect('livro', livro_id=livro.id)  # Redirecione para uma view adequada
    return redirect('livros')  # Caso não seja POST
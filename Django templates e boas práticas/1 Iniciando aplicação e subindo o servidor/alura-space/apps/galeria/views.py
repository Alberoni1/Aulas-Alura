from django.shortcuts import render, get_object_or_404,redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario Não Logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request,'galeria/index.html', {'cards':fotografias})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request,'galeria/imagem.html', {'fotografia':fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuario Não Logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html',{'cards':fotografias})

def upload_foto(request):
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            fotografia = form.save(commit=False)
            # Se desejar associar o usuário autenticado, por exemplo:
            if request.user.is_authenticated:
                fotografia.usuario = request.user
            fotografia.save()

            messages.success(request, 'Upload realizado com sucesso!')

            return redirect('upload_foto')  # Altere para a URL desejada
    else:
        form = FotografiaForm()
    return render(request, 'galeria/upload_foto.html', {'form': form})

def edit_foto(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto alterada com sucesso!')
            return redirect('index')
    return render(request, 'galeria/edit_foto.html', {'form': form, 'foto_id': foto_id})

def remover_foto(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Foto removida com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': fotografias})

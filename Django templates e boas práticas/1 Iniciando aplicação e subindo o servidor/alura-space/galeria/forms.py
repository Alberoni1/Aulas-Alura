from django import forms
from galeria.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = ['nome', 'legenda', 'categoria', 'descricao', 'foto', 'data_fotografia']
        # Caso você queira definir o usuário automaticamente (ex: request.user), não inclua 'usuario'
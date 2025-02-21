from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite seu Usuario'
            }
        )
    )

    senha =  forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    usuario1 = forms.CharField(
        label = 'Nome de Usuário',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex. usuario1'
            }
        )
    )
    
    primeiro_nome = forms.CharField(
        label = 'Primeiro Nome',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex. João'
            }
        )
    )

    segundo_nome = forms.CharField(
        label = 'Ultimo Nome',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex. Silva'
            }
        )
    )

    email = forms.EmailField(
        label = 'Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ex. nome@ummail.com'
            }
        )
    )
    
    senha =  forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    confirmasenha = forms.CharField(
        label='Confirmação de Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    def clean_usuario1(self):
        nome = self.cleaned_data.get('usuario1')
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Não é possivel conter espaços no usuario')
            else:
                return nome
        

    
    def clean_confirmasenha(self):
        senha1 = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('confirmasenha')

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('SENHAS DIFERENTES')
            else:
                return senha2
            

    
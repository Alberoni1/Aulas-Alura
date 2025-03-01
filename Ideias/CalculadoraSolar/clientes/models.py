from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_file_size(value):
    max_size = 5 * 1024 * 1024  # 5MB
    if value.size > max_size:
        raise ValidationError("O arquivo não pode exceder 5MB.")

def validate_file_mimetype(value):
    allowed_mimetypes = [
        'application/pdf',  # PDF
        'image/jpeg',       # JPG/JPEG
        'image/png',        # PNG
        'image/gif'         # GIF
    ]
    if value.file.content_type not in allowed_mimetypes:
        raise ValidationError("Apenas arquivos PDF ou imagens (JPG, PNG, GIF) são permitidos.")

class ClientePF(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True,verbose_name='CPF')
    email = models.EmailField(max_length=200,blank=False,null=False)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)
    data_cadastro = models.DateField(default=datetime.now,blank=False)
    
    class Meta:
        verbose_name_plural = 'Clientes PF'

    def __str__(self):
        return self.nome
    
class ClientePJ(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True,verbose_name='CNPJ ')
    email = models.EmailField(max_length=200,blank=False,null=False)
    celular = models.CharField(max_length=14)
    data_cadastro = models.DateField(default=datetime.now,blank=False)
    
    class Meta:
        verbose_name_plural = 'Clientes PJ'

    def __str__(self):
        return self.nome
    
class ContaClientePFFile(models.Model):
    cliente = models.ForeignKey(ClientePF, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'gif']),
            validate_file_mimetype,
            validate_file_size
        ],
        verbose_name="Arquivo (PDF ou imagem)"
    )
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.arquivo.name}"
    
class ContaClientePJFile(models.Model):
    cliente = models.ForeignKey(ClientePJ, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(
        upload_to='uploadspj/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png', 'gif']),
            validate_file_mimetype,
            validate_file_size
        ],
        verbose_name="Arquivo (PDF ou imagem)"
    )
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.arquivo.name}"
    

    
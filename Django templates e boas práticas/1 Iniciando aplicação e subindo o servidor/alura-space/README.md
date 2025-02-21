# 📌 Configurando o Django para armazenar arquivos no Amazon S3

Este guia explica como configurar o **Django 5.1.6** para armazenar arquivos estáticos e de mídia no **Amazon S3** utilizando `django-storages`.

---

## 📦 1. Instalação das Dependências

Execute os seguintes comandos para instalar as bibliotecas necessárias:

```bash
pip install boto3 django-storages python-dotenv
```

Adicione `storages` ao `INSTALLED_APPS` no `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'storages',
]
```

---

## 🔑 2. Configuração das Credenciais AWS

Crie um arquivo **`.env`** e adicione suas credenciais da AWS:

```ini
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=SUA_SECRET_KEY
AWS_STORAGE_BUCKET_NAME=seu-bucket
AWS_S3_REGION_NAME=sa-east-1  # Região do seu bucket
```

No `settings.py`, carregue as variáveis de ambiente:

```python
from dotenv import load_dotenv
import os

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "sa-east-1")

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_QUERYSTRING_AUTH = False  # Remove parâmetros de autenticação da URL
```

---

## 📂 3. Configuração do Storage no Django

A partir do **Django 4.2**, usamos `STORAGES` para configurar múltiplos storages:

```python
STORAGES = {
    "default": {  # Mídia (uploads de usuários)
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_S3_REGION_NAME,
            "location": "media",
            "default_acl": "private",
        },
    },
    "staticfiles": {  # Arquivos estáticos (CSS, JS, imagens do frontend)
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_S3_REGION_NAME,
            "location": "static",
            "default_acl": "public-read",
        },
    },
}
```

Defina os paths corretos para mídia e estáticos:

```python
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
```

---

## 🔄 4. Atualização e Coleta de Arquivos

### **Enviar arquivos estáticos para o S3:**

```bash
python manage.py collectstatic
```

Esse comando enviará todos os arquivos estáticos para o bucket S3.

### **Testar Upload de Imagem no Django**

Abra um shell Django:

```bash
python manage.py shell
```

E execute:

```python
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.galeria.models import Foto

foto = Foto.objects.create(imagem=SimpleUploadedFile("teste.jpg", b"conteudo"))
print(foto.imagem.url)  # Deve retornar uma URL do S3
```

Se a URL apontar para o **Amazon S3**, significa que tudo está funcionando corretamente. 🚀

---

## 🛠 5. Debugging e Possíveis Problemas

### ❌ **Problema: As imagens estão sendo salvas em `static/` em vez de `media/`**
✅ **Solução:** Confirme que `STORAGES["default"]` tem `"location": "media"`.

### ❌ **Problema: Arquivos não carregam no navegador**
✅ **Solução:** Verifique se o bucket está configurado como "Público" ou se o `default_acl` está definido corretamente (`public-read`).

### ❌ **Problema: CSS e JavaScript não estão carregando**
✅ **Solução:** Execute `python manage.py collectstatic` e confirme que os arquivos foram enviados para `static/` no S3.

---

## ✅ Conclusão
Agora o **Django 5.1.6** está configurado para armazenar arquivos no **Amazon S3**! 🎉



Para cadastrar o Client_ID e a Secret do GITHUB no .env, no arquivo, foi usado variaveis como:
        SECRET_KEY=django-insecure-....
        GITHUB_CLIENT_ID= Client_ID (sendo 'Client_ID' o valor dado pelo GITHUB)
        GITHUB_SECRET= secret(sendo 'secret' o valor dado pelo GITHUB)

para chamar foi incluido no settings.py:

    import os
    from dotenv import load_dotenv

depois:

    load_dotenv()  que Carrega as variáveis do .env

e então, nas linhas de código :

    SOCIALACCOUNT_PROVIDERS = {
        "github": {
            "APP": {
                "client_id": os.getenv("GITHUB_CLIENT_ID"),
                "secret": os.getenv("GITHUB_SECRET"),
                "key": "",
            }
        }
    }

Para gerenciar as paginas ao fazer login e logout, foram adicionadas as linhas:


    LOGIN_REDIRECT_URL = '/members' "que redireciona para a pagina 'members' do site após o login"

    SOCIALACCOUNT_LOGIN_ON_GET = True "Retira a pagina intermediaria do Allauth ao fazer o login"

    ACCOUNT_LOGOUT_ON_GET = True "Retira a pagina intermediaria do Allauth ao fazer o logout"



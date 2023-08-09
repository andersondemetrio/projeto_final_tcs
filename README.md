## Projeto Final de Conclusão de Curso

### Criando as variaveis de ambiente (.env) na razi do projeto:

```bash
touch .env

EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=usuario@gmail.com
EMAIL_HOST_PASSWORD=senha_usuario
DEFAULT_FROM_EMAIL=email_default.com
```

### Criando um ambiente virtual (virtual env)

```bash
# crie o env:
python -m venv venv .

# ative o ambiente no windows
venv\Scripts\activate

# faça a instalação das dependencias listadas no arquivo requirements.txt
pip -r install requirements.txt

# Faça a migração da aplicação
python manage.py migrate

# inicie o serviço

python manage.py runserver
```


## Projeto Final de Conclusão de Curso

### Criando as variaveis de ambiente (.env) na raiz do projeto:

```bash
touch .env

EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=usuario@gmail.com
EMAIL_HOST_PASSWORD=senha_usuario
DEFAULT_FROM_EMAIL=email_default.com
```

### Banco de dados
```
Roder o seguinte comando em docker
docker run --name teste -e POSTGRES_PASSWORD=teste -e POSTGRES_DB=teste -p 5432:5432 -d postgres
```

### Criando um ambiente virtual (virtual env)

```bash
# crie o env:
python -m venv venv .

# ative o ambiente no windows
venv\Scripts\activate

# faça a instalação das dependencias listadas no arquivo requirements.txt
pip  install -r requirements.txt

# Faça a migração da aplicação
python manage.py migrate

# inicie o serviço

python manage.py runserver

docker run --name teste -e POSTGRES_PASSWORD=teste -e POSTGRES_DB=teste -p 5432:5432 -d postgres
```

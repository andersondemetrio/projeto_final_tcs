"# Projeto Final de Conclusão de Curso" 

# crie um ambiente virtual

python -m venv venv .

ative o ambiente no windows

venv\Scripts\activate

faça a instalação do arquivo requirements.txt

pip -r install requirements.txt

faça a migração da aplicaçaõ

python manage.py migrate

roder o serviço

python manage.py runserver

Crie o arquivo .env na raiz do projeto

EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=usuario@gmail.com
EMAIL_HOST_PASSWORD=senha_usuario
DEFAULT_FROM_EMAIL=email_default.com

Roder o seguinte comando em docker
docker run --name teste -e POSTGRES_PASSWORD=teste -e POSTGRES_DB=teste -p 5432:5432 -d postgres
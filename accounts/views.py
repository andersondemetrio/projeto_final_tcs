from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import logging

import string

from django.core.mail import send_mail
from django.conf import settings
import random


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Definir o formato de registro
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Criar um manipulador de registro para registrar no arquivo
file_handler = logging.FileHandler('email_log.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Criar um manipulador de registro para exibir registros no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciais inválidas.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

def landing_page_view(request):
    return render(request, 'landing_page.html')

def primeiro_acesso(request):
    return render(request, 'primeiro_acesso.html') # Redireciona para a página de primeiro acesso

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html') # Redireciona para a página de recuperar senha

# inclusão da condiguração de envio de e-mail

logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)


def enviar_email_cadastro(request):
    logger = logging.getLogger('django')  # Crie um logger com o nome 'django'
    
    logger.setLevel(logging.DEBUG)
    mensagem_email = ''  # Inicializa a variável mensagem_email com uma string vazia

    if request.method == 'POST':
        user_email = request.POST.get('email')
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        link_cadastro = f'http://127.0.0.1:8000/login'
       # mensagem_email = f'Olá! Você pode concluir seu cadastro no RPrice clicando no seguinte link: {link_cadastro}'

        # use a função gerar_senha_aleatoria para enviar junto com o e-mail de cadastro
        senha_aleatoria = gerar_senha_aleatoria()
        mensagem_email = f'Olá! Você pode concluir seu cadastro no RPrice clicando no seguinte link: {link_cadastro} e sua senha é: {senha_aleatoria}'
       

        send_mail(
            'Conclua seu cadastro no RPrice',
            mensagem_email,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=True,
        )

        return render(request, 'pagina_email_enviado.html')  # Renderiza o template 'pagina_email_enviado.html'

    return render(request, 'enviar_email_cadastro.html', {'mensagem_email': mensagem_email})

from django.shortcuts import redirect

def redirect_to_custom_login(request):
    next_url = request.GET.get('next', '')
    if next_url:
        return redirect(f'/login/?next={next_url}')
    return redirect('/login/')

# crie uma função para gerar senha aleatória

def gerar_senha_aleatoria():
    # Definir todos os caracteres que serão usados para gerar a senha
    caracteres = string.ascii_letters + string.digits
    # Definir o tamanho da senha
    tamanho = random.randint(8, 16)
    # Gerar a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
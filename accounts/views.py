from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging


import string

from django.core.mail import send_mail
from django.conf import settings
import random


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

@login_required(redirect_field_name='login')
def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return HttpResponseNotFound('Página não encontrada.')

def primeiro_acesso(request):
    return render(request, 'primeiro_acesso.html') # Redireciona para a página de primeiro acesso

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html') # Redireciona para a página de recuperar senha

# inclusão da condiguração de envio de e-mail
def enviar_email_cadastro(request):
    logger = logging.getLogger('django')  # Crie um logger com o nome 'django'
    
    logger.setLevel(logging.DEBUG)
    mensagem_email = ''  # Inicializa a variável mensagem_email com uma string vazia

    if request.method == 'POST':
        user_email = request.POST.get('email')
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        link_cadastro = f'http://seusite.com/cadastro/?token={token}'
        mensagem_email = f'Olá! Você pode concluir seu cadastro no RPrice clicando no seguinte link: {link_cadastro}'

        send_mail(
            'Conclua seu cadastro no RPrice',
            mensagem_email,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=True,
        )

        return render(request, 'pagina_email_enviado.html')  # Renderiza o template 'pagina_email_enviado.html'

    return render(request, 'enviar_email_cadastro.html', {'mensagem_email': mensagem_email})
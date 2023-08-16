from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dashboard.models import Colaboradores
from django.db.models import Q
from django.conf import settings
import random
import logging
import string
from django.contrib.auth.views import PasswordResetView
from django.db.utils import IntegrityError

from django.core.mail import send_mail


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

def primeiro_acesso(request):
    return render(request, 'primeiro_acesso.html') # Redireciona para a página de primeiro acesso

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html') # Redireciona para a página de recuperar senha

# Primeiro acesso e inclusão da configuração de envio de e-mail

logger = logging.getLogger(__name__)

def enviar_email_cadastro(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        cpf_or_matricula = request.POST.get('login')
        
        colaborador = buscar_colaborador(cpf_or_matricula)
        if not colaborador:
            return colaborador_nao_encontrado(request)

        if usuario_ja_cadastrado(user_email):
            return email_ja_cadastrado(request)

        if colaborador.usuario:
            return colaborador_ja_cadastrado(request)

        senha_aleatoria = gerar_e_cadastrar_senha(colaborador, cpf_or_matricula, user_email)
        enviar_email_colaborador(user_email, senha_aleatoria)
        
        return render(request, 'email_enviado.html')

    return render(request, 'enviar_email_cadastro.html')

def enviar_email_colaborador(user_email, senha):
    link_cadastro = f'http://127.0.0.1:8000/login'
    mensagem_email = f'Olá! Você pode concluir seu cadastro no RPrice clicando no seguinte link: {link_cadastro} e sua senha é: {senha}'

    send_mail(
        'Conclua seu cadastro no RPrice',
        mensagem_email,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=True,
    )

def buscar_colaborador(cpf_or_matricula):
    try:
        return Colaboradores.objects.get(Q(cpf=cpf_or_matricula) | Q(matricula=cpf_or_matricula))
    except Colaboradores.DoesNotExist:
        return None

def colaborador_nao_encontrado(request):
    messages.error(request, 'Colaborador não encontrado.')
    return render(request, 'primeiro_acesso.html')

def usuario_ja_cadastrado(user_email):
    try:
        User.objects.get(email=user_email)
        return True
    except User.DoesNotExist:
        return False

def email_ja_cadastrado(request):
    messages.error(request, 'E-mail já cadastrado.')
    return render(request, 'primeiro_acesso.html')

def colaborador_ja_cadastrado(request):
    messages.info(request, 'Colaborador já está cadastrado.')
    return render(request, 'primeiro_acesso.html')

def gerar_e_cadastrar_senha(colaborador, cpf_or_matricula, user_email):
    senha_aleatoria = gerar_senha_aleatoria()
    novo_usuario = User.objects.create_user(username=cpf_or_matricula, email=user_email, password=senha_aleatoria)
    colaborador.usuario = novo_usuario
    colaborador.save()
    return senha_aleatoria

def gerar_senha_aleatoria():
    # Definir todos os caracteres que serão usados para gerar a senha
    caracteres = string.ascii_letters + string.digits
    # Definir o tamanho da senha
    tamanho = random.randint(8, 16)
    # Gerar a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Redefinições de senha

def redefinir_senha(request):
    return render(request, 'redefinir_senha.html')
    
def recuperar_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = validar_email(email)
        if user:
            PasswordResetView.as_view(
                template_name='registration/password_reset_form.html',  # Seu template de redefinição de senha
                email_template_name='registration/password_reset_email.html',  # Seu template de email
                success_url='email_recuperado'  # Nome da URL ou path para a página de confirmação
            )(request)
        else:
            messages.error(request, 'O E-mail não foi encontrado.')
            return render(request, 'recuperar_senha.html')
    return render(request, 'email_recuperado.html')

def validar_email(email):
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        return None

def redirect_to_custom_login(request):
    next_url = request.GET.get('next', '')
    if next_url:
        return redirect(f'/login/?next={next_url}')
    return redirect('/login/')

# Cadastro dos usuários no django

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        try:
            user = User.objects.create_superuser(username=username, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('cadastro_usuario_sucesso')  # Redirecionar para a página de sucesso
        except IntegrityError:  # Handle the case when a user with the same username already exists
            return render(request, 'cadastro_usuario.html', {'error_message': 'Usuário já existe'})

    return render(request, 'cadastro_usuario.html')

def cadastro_usuario_sucesso(request):
    return render(request, 'cadastro_usuario_sucesso.html')

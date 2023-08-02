from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User 

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()  # Remove espaços em branco no início e no final
        password = request.POST.get('password').strip()

        if not username or not password:
            messages.error(request, message='Usuário e/ou senha inválidos')
            return redirect('login')

        check_user = auth.authenticate(username=username, password=password)
        
        if check_user is None:
            messages.error(request, message='Usuário e/ou senha inválidos')
            return redirect('login')
        else:
            auth.login(request, check_user)
            return redirect('home')
        
    else:
        return render(request, 'pages/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        re_password = request.POST.get('re-password').strip()
        
        if not username or not email or not password or not re_password:
            messages.error(request, message='Preencha todos os campos')
            return redirect('cadastro')

        if password == re_password:
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('login')
    else:
        return render(request, 'pages/cadastro.html')

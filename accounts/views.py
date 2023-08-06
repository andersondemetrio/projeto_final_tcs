from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
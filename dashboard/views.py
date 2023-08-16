from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
import random
from .models import GastosFixos,Colaboradores,Cargos, Endereco, Empresa
from .forms import EmpresaForm

@login_required
def dashboard_view(request):
    if request.session.get('empresa_cadastrada'):
        success = True
        # Limpar a variável de sessão após verificar
        request.session['empresa_cadastrada'] = False
    else:
        success = False

    context = {
        # ... seu contexto existente ...
        'success': success,
    }
    if request.user.is_authenticated:
        return render(request, 'dashboard1.html')
    else:
        return render(request, 'account/login.html', context)

def inserir_gasto_fixo(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        GastosFixos.objects.create(descricao=descricao, valor=valor)
    return render(request, 'dashboard1.html', context={})

def inserir_mao_de_obra(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        salario = request.POST['salario']
        beneficios = request.POST['beneficios']
        encargos = request.POST['encargos']
        cargo_id = request.POST['cargo']  # Certifique-se de que esse é o nome correto do campo
        endereco_id = request.POST['endereco']

        cargo = Cargos.objects.get(id=cargo_id)
        
        mao_de_obra = Colaboradores(
            matricula=matricula,
            nome=nome,
            cpf=cpf,
            salario=salario,
            beneficios=beneficios,
            encargos=encargos,
            cargo=cargo,  # Associando o cargo à mão de obra
            endereco_id=endereco_id
        )
        mao_de_obra.save()
        return HttpResponse("Mão de obra cadastrada com sucesso!")

def cargos_vieww(request):
    cargos = Cargos.objects.all()
    cargos_list = [{'id': cargo.id, 'nome_cargo': cargo.nome_cargo} for cargo in cargos]
    return JsonResponse({'cargos': cargos_list})

# funciona, mas não mostra o resultado
# def endereco_view(request):
#     enderecos = Endereco.objects.all()
#     enderecos_list = [{'id': endereco.id, 'endereco': endereco.endereco} for endereco in enderecos]
#     return JsonResponse({'enderecos': enderecos_list})

def endereco_view(request):
    enderecos = Endereco.objects.all()
    enderecos_list = [
        {
            'id': endereco.id,
            'endereco': f"{endereco.logradouro}, {endereco.numero}, {endereco.complemento}, {endereco.bairro}, {endereco.cidade}, {endereco.estado}"
        }
        for endereco in enderecos
    ]
    return JsonResponse({'enderecos': enderecos_list})

def inserir_empresa(request):
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        numero_empresa = request.POST['numero_empresa']
        nome_empresa = request.POST['nome_empresa']
        nome_fantasia = request.POST['nome_fantasia']
        email = request.POST['email']
        telefone = request.POST['telefone']
        ativa = request.POST.get('ativa') == 'on'  # Verifica se a checkbox foi marcada
        endereco_id = request.POST['endereco']

        empresa = Empresa(
            cnpj=cnpj,
            numero_empresa=numero_empresa,
            nome_empresa=nome_empresa,
            nome_fantasia=nome_fantasia,
            email=email,
            telefone=telefone,
            ativa=ativa,
            endereco_id=endereco_id
        )
        
        empresa.save()
        request.session['empresa_cadastrada'] = True
        return redirect('dashboard')

    return render(request, 'dashboard1.html', context={})
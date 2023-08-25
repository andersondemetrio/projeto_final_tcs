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
from django.core.paginator import Paginator

from django.core.mail import send_mail
from django.conf import settings
import random
from .models import GastosFixos,Colaboradores,Cargos, Endereco, Empresa,CalendarioMensal

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
        return redirect('dashboard')
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
        # endereco_id = request.POST['endereco']

        cargo = Cargos.objects.get(id=cargo_id)
        
        mao_de_obra = Colaboradores(
            matricula=matricula,
            nome=nome,
            cpf=cpf,
            salario=salario,
            beneficios=beneficios,
            encargos=encargos,
            cargo=cargo,  # Associando o cargo à mão de obra
            # endereco_id=endereco_id
        )
        mao_de_obra.save()
        return HttpResponse("Mão de obra cadastrada com sucesso!")

# Funções do CRUD de cargos

def inserir_cargo(request):
    if request.method == 'POST':
        nome_cargo = request.POST['nome_cargo']

        cargo = Cargos(
            nome_cargo=nome_cargo,
        )
        
        cargo.save()
        return redirect('dashboard')

    return render(request, 'dashboard1.html', context={}) 

def editar_cargo(request):
    cargo = Cargo.objects.get(pk=cargo_id)
    if request.method == 'POST':
        nome_cargo = request.POST.get['nome_cargo']

        cargo.nome_cargo = nome_cargo
        
        cargo.save()
        return redirect('dashboard')

    return render(request, 'dashboard1.html', context={}) 

def cargos_vieww(request):
    cargos = Cargos.objects.all()
    cargos_list = [{'id': cargo.id, 'nome_cargo': cargo.nome_cargo} for cargo in cargos]
    return JsonResponse({'cargos': cargos_list})

def deletar_cargo(request, cargo_id):
    if request.method == 'POST':
        try:
            cargo = Cargos.objects.get(pk=cargo_id)
            cargo.delete()
            return redirect('dashboard')
        except Cargo.DoesNotExist:
            return JsonResponse({"success": False, "error": "Registro não encontrado"})
    else:
        try:
            cargo = Cargos.objects.get(pk=cargo_id)
            return render(request, 'confirm_delete.html')
        except cargo.DoesNotExist:
            return JsonResponse({"success": False, "error": "Registro não encontrado"})

# Funções do CRUD de endereços

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
        # request.session['empresa_cadastrada'] = True
        return redirect('dashboard')

    return render(request, 'dashboard1.html', context={})

def inserir_endereco(request):
    if request.method == 'POST':
        logradouro = request.POST['logradouro']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        Endereco.objects.create(logradouro=logradouro, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, 
                                estado=estado)
        return redirect('dashboard')
    return render(request, 'dashboard1.html', context={})

# @login_required
def alterar_senha(request):
    if request.method == 'POST':
        nova_senha = request.POST.get('novaSenha')
        repetir_senha = request.POST.get('repetirSenha')

        if nova_senha == repetir_senha:
            user = request.user
            user.set_password(nova_senha)
            user.save()
            
            # Atualiza a sessão de autenticação para evitar logout automático
            # update_session_auth_hash(request, user)

            messages.success(request, 'Senha alterada com sucesso.')
            return redirect('login')
        else:
            messages.error(request, 'As senhas não coincidem.')
    return render(request, 'dashboard1.html', {'keep_modal_open': True})

def inserir_beneficio(request):
    return render(request, 'dashboard1.html', context={})

def inserir_encargo(request):
    return render(request, 'dashboard1.html', context={})

def inserir_data(request):
    return render(request, 'dashboard1.html', context={})    

def inserir_jornada(request):
    return render(request, 'dashboard1.html', context={})

def inserir_horas(request):
    return render(request, 'dashboard1.html', context={})       



# Função para validar a inserção dos dias uties e horas produtiva do mes 

def inserir_calendario(request):
    if request.method == "POST":
        mes = int(request.POST.get("mes"))
        ano = int(request.POST.get("ano"))
        jornada_diaria = float(request.POST.get("jornada_diaria"))
        funcionario_id = int(request.POST.get("funcionario"))
        horas_produtivas = float(request.POST.get("horas_produtivas"))
        dias_uteis = int(request.POST.get("dias_uteis"))  # Pegar o valor dos dias úteis

        funcionario = Colaboradores.objects.get(pk=funcionario_id)

        calendario = CalendarioMensal(
            mes=mes,
            ano=ano,
            jornada_diaria=jornada_diaria,
            funcionario=funcionario,
            horas_produtivas=horas_produtivas,
            dias_uteis=dias_uteis  # Definir o valor dos dias úteis
        )
        calendario.save()

        return redirect("dashboard")  # Redirecionar para uma página de sucesso

    return render(request, "dashboard1.html")

# funçaõ para listar os colaboradores no select do calendario
def colaboradores_view(request):
    colaboradores = Colaboradores.objects.all()
    colaboradores_list = [{'id': colaborador.id, 'nome': colaborador.nome} for colaborador in colaboradores]
    return JsonResponse({'colaboradores': colaboradores_list})

def search(request): 
    q = request.GET.get('search')   
    cargos = Cargos.objects.filter(nome_cargo__icontains=q)
    
    paginator = Paginator(cargos, 100)  # 5 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'pesquisa_cargo.html', {'page_obj': page_obj})
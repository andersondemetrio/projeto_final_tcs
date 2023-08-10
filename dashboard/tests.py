# from django.test import TestCase

# # Create your tests here.

# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")  # Substitua "projeto.settings" pelo caminho correto para o seu arquivo settings.py
# django.setup()

# from dashboard.models import Endereco, Usuarios, Cargos, HorasProdutivas, GastosFixos, Insumos, Empresa, Colaboradores, GastosVariaveis, Propostas

# def insert_data():
#     # Inserir registros em todas as tabelas
#     endereco = Endereco.objects.create(cep="12345-678", logradouro="Rua X", endereco="Rua Principal", numero="123",
#                                        complemento="Bloco A", bairro="Centro", cidade="Cidade", estado="Estado")

#     usuario = Usuarios.objects.create(email="usuario@example.com", senha="senha123", permissao="admin")

#     cargo = Cargos.objects.create(nome_cargo="Gerente")

#     horas_produtivas = HorasProdutivas.objects.create(data="2023-08-10", jornada_diaria=8.0)

#     gasto_fixo = GastosFixos.objects.create(descricao="Aluguel", valor=1000.0)

#     insumo = Insumos.objects.create(descricao="Papel", valor=10.0)

#     empresa = Empresa.objects.create(cnpj="12345678901234", numero_empresa=1, nome_empresa="Minha Empresa",
#                                      nome_fantasia="Empresa Fantasia", email="contato@empresa.com", telefone="1234567890",
#                                      ativa=True, endereco=endereco)

#     colaborador = Colaboradores.objects.create(nome="João Silva", matricula="123456", cpf="123.456.789-00",
#                                                cargo=cargo, salario=5000.0, beneficios=500.0, encargos=1000.0,
#                                                endereco=endereco)

#     gasto_variavel = GastosVariaveis.objects.create(colaborador=colaborador, insumo=insumo, quantidade=50.0)

#     proposta = Propostas.objects.create(usuario=usuario, data_proposta="2023-08-10", aprovada=True)

#     # Exibir os registros inseridos
#     print("Registros inseridos:")
#     print("Endereço:", endereco)
#     print("Usuário:", usuario)
#     print("Cargo:", cargo)
#     print("Horas Produtivas:", horas_produtivas)
#     print("Gasto Fixo:", gasto_fixo)
#     print("Insumo:", insumo)
#     print("Empresa:", empresa)
#     print("Colaborador:", colaborador)
#     print("Gasto Variável:", gasto_variavel)
#     print("Proposta:", proposta)

# if __name__ == "__main__":
#     insert_data()
from django.test import TestCase
from .models import Endereco, Usuarios, Cargos, HorasProdutivas, GastosFixos, Insumos, Empresa, Colaboradores, GastosVariaveis, Propostas

class ModelTests(TestCase):
    def test_criar_endereco(self):
        endereco = Endereco.objects.create(cep="12345-678", logradouro="Rua X", endereco="Rua Principal", numero="123",
                                           complemento="Bloco A", bairro="Centro", cidade="Cidade", estado="Estado")
        self.assertEqual(endereco.cep, "12345-678")
        self.assertEqual(endereco.logradouro, "Rua X")
        # Adicione mais asserções conforme necessário

    def test_criar_usuario(self):
        usuario = Usuarios.objects.create(email="usuario@example.com", senha="senha123", permissao="admin")
        self.assertEqual(usuario.email, "usuario@example.com")
        self.assertEqual(usuario.senha, "senha123")
        # Adicione mais asserções conforme necessário

    def test_criar_cargo(self):
        cargo = Cargos.objects.create(nome_cargo="Gerente")
        self.assertEqual(cargo.nome_cargo, "Gerente")
        # Adicione mais asserções conforme necessário

        #faz um select no banco e verifica se o valor é igual ao esperado
    def validar_usuario(self):
        usuario = Usuarios.objects.get(email="")
        self.assertEqual(usuario.email,"")
        #print resultado
        self.stdout.write(f"Email do usuário: {usuario.email}")

    # Adicione mais métodos de teste para outros modelos aqui

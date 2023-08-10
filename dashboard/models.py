from django.db import models

'''
Modifique o códgio sql abaixo para o model do django

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    permissao VARCHAR(50) NOT NULL
);

CREATE TABLE cargos (
    id_cargo SERIAL PRIMARY KEY,
    nome_cargo VARCHAR(100) NOT NULL
);

CREATE TABLE horas_produtivas (
    id_horas SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    jornada_diaria NUMERIC(5, 2) NOT NULL
);

CREATE TABLE gastos_fixos (
    id_gastos_fixos SERIAL PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL
);

CREATE TABLE insumos (
    id_insumo SERIAL PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    valor NUMERIC(10, 2) NOT NULL
);

CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
	cep VARCHAR(9) NOT NULL,
	logradouro VARCHAR(15) NOT NULL,
	endereco VARCHAR(40) NOT NULL,
	numero VARCHAR(10) NOT NULL,
	complemento VARCHAR(30) NOT NULL,
	bairro VARCHAR(30) NOT NULL,
	cidade VARCHAR(30) NOT NULL,
	estado VARCHAR(30) NOT NULL
);

CREATE TABLE empresa (
    id_empresa SERIAL PRIMARY KEY,
	cnpj VARCHAR(18) NOT NULL,
	numero_empresa NUMERIC(3) NOT NULL,
    nome_empresa VARCHAR(100) NOT NULL,
	nome_fantasia VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	telefone VARCHAR(15) NOT NULL,
	ativa BOOLEAN NOT NULL,
	id_endereco INTEGER REFERENCES endereco(id_endereco)
);

CREATE TABLE colaboradores (
    id_colaborador SERIAL PRIMARY KEY,
    nome  VARCHAR(100) NOT NULL,
	matricula VARCHAR(12) NOT NULL,
	cpf VARCHAR(14) NOT NULL,
    id_cargo INTEGER REFERENCES cargos(id_cargo),
    salario NUMERIC(10, 2) NOT NULL,
    beneficios NUMERIC(10, 2) NOT NULL,
    encargos NUMERIC(10, 2) NOT NULL,
	id_endereco INTEGER REFERENCES endereco(id_endereco)
);


CREATE TABLE gastos_variaveis (
    id_gastos_variaveis SERIAL PRIMARY KEY,
    id_colaborador INTEGER REFERENCES colaboradores(id_colaborador),
    id_insumo INTEGER REFERENCES insumos(id_insumo),
    quantidade NUMERIC(10, 2) NOT NULL
);

CREATE TABLE propostas (
    id_proposta SERIAL PRIMARY KEY,
    id_usuario INTEGER REFERENCES usuarios(id_usuario),
    data_proposta DATE NOT NULL,
    aprovada BOOLEAN NOT NULL
);


'''

from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=15)
    endereco = models.CharField(max_length=40)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)

class Usuarios(models.Model):
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    permissao = models.CharField(max_length=50)

class Cargos(models.Model):
    nome_cargo = models.CharField(max_length=100)

class HorasProdutivas(models.Model):
    data = models.DateField()
    jornada_diaria = models.DecimalField(max_digits=5, decimal_places=2)

class GastosFixos(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Insumos(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Empresa(models.Model):
    cnpj = models.CharField(max_length=18)
    numero_empresa = models.DecimalField(max_digits=3, decimal_places=0)
    nome_empresa = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    ativa = models.BooleanField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class Colaboradores(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=12)
    cpf = models.CharField(max_length=14)
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.DecimalField(max_digits=10, decimal_places=2)
    encargos = models.DecimalField(max_digits=10, decimal_places=2)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class GastosVariaveis(models.Model):
    colaborador = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

class Propostas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    data_proposta = models.DateField()
    aprovada = models.BooleanField()

from django.db import models
from datetime import datetime, date

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    # data_cadastro = models.DateTimeField(default=datetime.today)
    # data_atualizacao = models.DateTimeField(default=datetime.today)
    email = models.EmailField()
    senha = models.CharField(max_length=128)
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=80)
    telefone = models.CharField(max_length=11)
class Vendedor(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=80)
    # data_nascimento = models.DateField()
    sexo = models.CharField(max_length=2)
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=80)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=30)
    complemento = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
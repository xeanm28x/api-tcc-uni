from django.db import models
from datetime import datetime
from usuario.models import Cliente

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(default=datetime.today)
    data_atualizacao = models.DateTimeField(default=datetime.today)
    valor_total = models.FloatField(default=0)
    opcoes_forma_pagamento = (
        ('Dinheiro', 'Dinheiro'),
        ('Crédito', 'Crédito'),
        ('Débito', 'Débito'),
        ('PIX', 'PIX')
    )
    forma_pagamento = models.CharField(max_length=15, choices=opcoes_forma_pagamento)
    data_prevista_entrega = models.DateTimeField(null=True)
    data_entrega = models.DateTimeField(null=True)
    logradouro = models.CharField(max_length=80, null=True)
    numero = models.CharField(max_length=6, null=True)
    bairro = models.CharField(max_length=30, null=True)
    complemento = models.CharField(max_length=30, null=True)
    valor_promocional = models.FloatField(null=True)
    opcoes_status = (
        ('Novo', 'Novo'),
        ('Em andamento', 'Em andamento'),
        ('Cancelado', 'Cancelado'),
        ('Concluido', 'Concluido')
    )
    status = models.CharField(max_length=15, choices=opcoes_status)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

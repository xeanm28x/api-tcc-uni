from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    valor_unitario = models.FloatField(null=False)
    ativo = models.BooleanField(default=True)

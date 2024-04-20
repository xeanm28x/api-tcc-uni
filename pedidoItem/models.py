from django.db import models
from datetime import datetime
from produto.models import Produto
from pedido.models import Pedido

class PedidoItem(models.Model):
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(default=datetime.today)
    data_atualizacao = models.DateTimeField(default=datetime.today)
    quantidade = models.IntegerField(null=True)
    comentario = models.CharField(max_length=128, null=True)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)

from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .models import PedidoItem
from produto.models import Produto
from pedido.models import Pedido
import json

@csrf_exempt 
def store(request):
    try:
        if request.method == "POST":
            item = json.loads(request.body)
            if not item:
                raise ValueError("Erro ao processar requisição")
            if "id_produto" not in item or "id_pedido" not in item:
                raise ValueError("Produto e pedido obrigatórios")
            pedidoBD = Pedido.objects.filter(id=item["id_pedido"]).first()
            if not pedidoBD or pedidoBD.status in ["Em andamento", "Concluido", "Cancelado"]:
                raise KeyError("Pedido inválido")
            produtoBD = Produto.objects.filter(id=item["id_produto"]).first()
            if not produtoBD:
                raise KeyError("Produto inválido")
            if "quantidade" not in item:
                raise ValueError("Quantidade obrigatória")
            if item["quantidade"] == 0:
                raise ValueError("Quantidade inválida")
            itemBD = PedidoItem.objects.filter(id_produto=produtoBD.id, id_pedido=pedidoBD.id).first()
            if itemBD:
                itemBD.quantidade += item["quantidade"]
                itemBD.save()
                itemBD = json.loads(serialize("json", [itemBD]))
                retorno = json.dumps({
                    "success": True,
                    "message": "Item adicionado com sucesso!",
                    "item": json.dumps(itemBD[0]["fields"])
                })
            else:
                pedidoItem = PedidoItem(
                id_produto = produtoBD,
                id_pedido = pedidoBD
                )
                pedidoItem.quantidade = item["quantidade"]
                if "comentario" in item:
                    pedidoItem.comentario = item["comentario"]
                pedidoItem.save()
                item = json.loads(serialize("json", [pedidoItem]))
                retorno = json.dumps({
                    "success": True,
                    "message": "Item adicionado com sucesso!",
                    "item": json.dumps(item[0]["fields"])
                })
            return HttpResponse(content=retorno, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
@csrf_exempt
def index(request):
    try:
        if request.method == "GET":
            id_pedido = request.GET.get("id_pedido")
            itens = PedidoItem.objects.filter(id_pedido=id_pedido).all()
            itens = json.loads(serialize('json', itens))
            itens = json.dumps(itens)
            return HttpResponse(content=itens, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
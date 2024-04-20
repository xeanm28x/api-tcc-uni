from django.http import HttpResponse
from django.core.serializers import serialize
from pedido.models import Pedido
from usuario.models import Cliente
import json

def store(request):
    try:
        if request.method == "POST":
            pedido = json.loads(request.body)
            if not pedido:
                raise ValueError("Erro ao processar requisição")
            if "forma_pagamento" not in pedido or "id_cliente" not in pedido:
                raise ValueError("Por gentileza, preencher dados obrigatórios")
            if pedido["forma_pagamento"] not in ["Dinheiro", "Débito", "Crédito", "PIX"]:
                raise ValueError("Forma de pagamento inválida")
            clienteBD = Cliente.objects.filter(id=pedido["id_cliente"]).first()
            if not clienteBD:
                raise KeyError("Cliente inválido")
            novoPedido = Pedido(
                id_cliente = clienteBD,
                forma_pagamento = pedido["forma_pagamento"],
                status = "Novo"
            )
            if "logradouro" in pedido:
                novoPedido.logradouro = pedido["lograouro"]
            if "numero" in pedido:
                novoPedido.numero = pedido["numero"]
            if "bairro" in pedido:
                novoPedido.bairro = pedido["bairro"]
            if "complemento" in pedido:
                novoPedido.complemento = pedido["complemento"]
            if "valor_promocional" in pedido:
                novoPedido.valor_promocional = pedido["valor_promocional"]
            novoPedido.save()
            return HttpResponse(content="Pedido realizado com sucesso!", status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
def index(request):
    try:
        if request.method == "GET":
            pedidos = Pedido.objects.all()
            produtos = json.loads(serialize('json', pedidos))
            produtos = json.dumps(produtos)
            return HttpResponse(content=produtos, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
def show(request):
    try:
        if request.method == "GET":
            id = request.GET.get("id")
            if not id:
                raise KeyError("Pedido inválido")
            pedido = Pedido.objects.filter(id=id).all()
            if not pedido:
                raise KeyError("Pedido não encontrado")
            pedido = json.loads(serialize("json", pedido))
            pedido = json.dumps(pedido[0]["fields"])
            return HttpResponse(content=pedido, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
def update(request):
    try:
        pedido = json.loads(request.body)
        if not pedido:
            raise ValueError("Pedido não informado")
        if "id" not in pedido or "status" not in pedido:
            raise ValueError("Erro ao processar requisição")
        pedidoBD = Pedido.objects.filter(id=pedido["id"]).first()
        if not pedidoBD:
            raise ValueError("Pedido inexistente")
        if len(pedido) == 2:
            raise UserWarning("Sem novos valores para atualizar.")
        if pedidoBD.status in ["Em andamento", "Concluido", "Cancelado"]:
            raise ValueError(f"Não é possível alterar o pedido. Status: {pedidoBD.status}")
        if "valor_total" in pedido and pedidoBD.valor_total != pedido["valor_total"]:
            raise ValueError("Não é possível alterar o valor total.")
        if pedido["status"] == "Cancelado":
            raise ValueError("Não é possível cancelar o pedido por aqui.")
        if "logradouro" in pedido:
            pedidoBD.logradouro = pedido["logradouro"]
        if "numero" in pedido:
            pedidoBD.numero = pedido["numero"]
        if "bairro" in pedido:
            pedidoBD.bairro = pedido["bairro"]
        if "complemento" in pedido:
            pedidoBD.complemento = pedido["complemento"]
        if "valor_promocional" in pedido:
            pedidoBD.valor_promocional = pedido["valor_promocional"]
        pedidoBD.status = pedido["status"]
        pedidoBD.save()
        pedido = json.loads(serialize("json", [pedidoBD]))
        retorno = json.dumps({
            "mensagem": "Pedido atualizado com sucesso!",
            "produto": json.dumps(pedido[0]["fields"])
            })
        return HttpResponse(content=retorno, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
def destroy(request):
    try:
        pedido = json.loads(request.body)
        if not pedido:
            raise ValueError("Por favor, informe o pedido a ser cancelado")
        if "id" not in pedido:
            raise ValueError("Erro ao processar requisição")
        pedidoBD = Pedido.objects.filter(id=pedido["id"]).first()
        if not pedidoBD:
            raise ValueError("Pedido inexistente")
        pedidoBD.status = "Cancelado"
        pedidoBD.save()
        return HttpResponse(content="Pedido cancelado com sucesso!", status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
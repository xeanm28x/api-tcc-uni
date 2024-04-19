from .models import Produto
from django.http import HttpResponse
from django.core.serializers import serialize
import json

def store(request):
    try:
        if request.method == "POST":
            novoProduto = json.loads(request.body)
            if not novoProduto:
                raise ValueError("Os campos obrigatórios precisam ser preenchidos")
            if "descricao" not in novoProduto or "valor_unitario" not in novoProduto:
                raise ValueError("Descrição e valor unitário são obrigatórios")
            novoProduto = Produto(
                descricao = novoProduto["descricao"],
                valor_unitario = novoProduto["valor_unitario"]
            )
            produtoBD = Produto.objects.filter(descricao=novoProduto.descricao).first()
            if produtoBD:
                raise ValueError("Produto já existente")
            novoProduto.save()
            return HttpResponse(content="Produto cadastrado com sucesso!", status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)

def index(request):
    try:
        if request.method == "GET":
            produtosAtivos = Produto.objects.filter(ativo=True).all()
            produtosInativos = Produto.objects.filter(ativo=False).all()
            produtosAtivos = json.loads(serialize('json', produtosAtivos))
            produtosInativos = json.loads(serialize('json', produtosInativos))
            produtosFields = {"ativos": [], "indisponiveis": []}
            for produto in produtosAtivos:
                produtosFields["ativos"].append(produto["fields"])
            for produto in produtosInativos:
                produtosFields["indisponiveis"].append(produto["fields"])
            produtosFields = json.dumps(produtosFields)
            return HttpResponse(content=produtosFields, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)

def show(request):
    try:
        if request.method == "GET":
            id = request.GET.get("id")
            produto = Produto.objects.filter(id=id).all()
            if not produto:
                raise KeyError("Produto não encontrado")
            produto = json.loads(serialize("json", produto))
            produto = json.dumps(produto[0]["fields"])
            return HttpResponse(content=produto, status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)

def update(request):
    try:
        produto = json.loads(request.body)
        if not produto:
            raise ValueError("Produto não informado")
        if "id" not in produto:
            raise ValueError("Erro ao processar requisição")
        produtoBD = Produto.objects.filter(id=produto["id"]).first()
        if not produtoBD:
            raise ValueError("Produto inexistente")
        if len(produto) == 1:
            raise UserWarning("Sem novos valores para atualizar.")
        if "descricao" in produto:
            produtoBD.descricao = produto["descricao"]
        if "valor_unitario" in produto:
            produtoBD.valor_unitario = produto["valor_unitario"]
        if "ativo" in produto:
            produtoBD.ativo = produto["ativo"]
        produtoBD.save()
        produto = json.loads(serialize("json", [produtoBD]))
        retorno = json.dumps({
            "mensagem": "Produto atualizado com sucesso!",
            "produto": json.dumps(produto[0]["fields"])
            })
        return HttpResponse(content=retorno, status=200)
    except Exception as erro:
        if erro.__class__ == UserWarning:
            return HttpResponse(content=erro, status=204)
        return HttpResponse(content=erro, status=400)

def destroy(request):
    try:
        produto = json.loads(request.body)
        if not produto:
            raise ValueError("Por favor, informe o produto a ser removido")
        if "id" not in produto:
            raise ValueError("Erro ao processar requisição")
        produtoBD = Produto.objects.filter(id=produto["id"]).first()
        if not produtoBD:
            raise ValueError("Produto inexistente")
        produtoBD.delete()
        return HttpResponse(content="Produto removido com sucesso!", status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
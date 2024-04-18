from django.shortcuts import render, redirect
from .models import Produto
from django.contrib import messages
from django.contrib.messages import constants
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@csrf_exempt
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

    return render(request, "")


def show(request):

    return render(request, "")


def update(request):

    return render(request, "")

@csrf_exempt
def destroy(request):
    try:
        produto = json.loads(request.body)
        if not produto:
            raise ValueError("Por favor, informe o produto a ser removido")
        if "id" not in produto:
            raise ValueError("Erro ao processar requisição")
        produtoBD = Produto.objects.filter(id=produto["id"]).first()
        if not produtoBD:
            raise ValueError("Produto inexistente.")
        produtoBD.delete()
        return HttpResponse(content="Produto removido com sucesso!", status=200)
    except Exception as erro:
        return HttpResponse(content=erro, status=400)
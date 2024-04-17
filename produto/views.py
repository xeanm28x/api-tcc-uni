from django.shortcuts import render, redirect
from .models import Produto
from django.contrib import messages
from django.contrib.messages import constants

def store(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        valor_unitario = request.POST.get('valor_unitario')
        produto = Produto(
            descricao = descricao,
            valor_unitario = valor_unitario
        )
        produto.save()
        messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso!')
        return redirect("/produto/index")

def index(request):

    return render(request, "")

def show(request):

    return render(request, "")

def update(request):

    return render(request, "")

def destroy(request):

    return render(request, "")
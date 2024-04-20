from django.contrib import admin
from .models import Administrador, Empresa, Cliente, Vendedor

admin.site.register(Administrador)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Vendedor)

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('usuario/', include('usuario.urls')),
    path('produto/', include('produto.urls')),
    path('pedido/', include('pedido.urls')),
    path('pedidoItem/', include('pedidoItem.urls'))
]

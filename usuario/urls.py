from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='store'),
    path('perfil/<int:id>', views.perfil, name='perfil'),
    path('update/<int:id>', views.update, name='update'),
    path('destroy/<int:id>', views.destroy, name='destroy')
]
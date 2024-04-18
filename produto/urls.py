from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('index/', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('update/', views.update, name='update'),
    path('destroy/', views.destroy, name='destroy')
]
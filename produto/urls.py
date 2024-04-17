from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('index/', views.index, name='index'),
    path('show/<int:id>', views.show, name='show'),
    path('update/<int:id>', views.update, name='update'),
    path('destroy/<int:id>', views.destroy, name='destroy')
]
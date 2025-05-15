from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
    path('gravarCompra/', views.gravarCompra, name='gravarCompra'),
]


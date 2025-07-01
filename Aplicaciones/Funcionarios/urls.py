from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioF),
    path('nuevoFuncionario/', views.nuevoFuncionario),
    path('guardarFuncionario/', views.guardarFuncionario),
    path('eliminarFuncionario/<id>/', views.eliminarFuncionario),
    path('editarFuncionario/<id>/', views.editarFuncionario),
    path('procesarEdicionFuncionario/<id>/', views.procesarEdicionFuncionario),
]

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.inicioU),
    path('nuevoUsuario/', views.nuevoUsuario),
    path('guardarUsuario/', views.guardarUsuario),
    path('eliminarUsuario/<id>/', views.eliminarUsuario),
    path('editarUsuario/<id>/', views.editarUsuario),
    path('procesarEdicionUsuario/<id>/', views.procesarEdicionUsuario),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioD),
    path('nuevaDenuncia/', views.nuevaDenuncia),
    path('guardarDenuncia/', views.guardarDenuncia),
    path('eliminarDenuncia/<id>/', views.eliminarDenuncia),
    path('editarDenuncia/<id>/', views.editarDenuncia),
    path('procesarEdicionDenuncia/<id>/', views.procesarEdicionDenuncia),
]

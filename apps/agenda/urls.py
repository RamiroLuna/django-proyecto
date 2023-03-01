from django.urls import path
from apps.agenda import views

urlpatterns = [
    path('', views.home),
    path('registrarDatos/', views.registrarDatos),
    path('edicionDatos/<id>', views.edicionDatos),
    path('editarDatos/', views.editarDatos),
    path('eliminarDatos/<id>', views.eliminarDatos)
]
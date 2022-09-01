from django.urls import path

from Constructora import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('cliente', views.clientes, name="Cliente"),
    
]

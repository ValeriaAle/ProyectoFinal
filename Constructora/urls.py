from django.urls import path

from Constructora import views


urlpatterns = [

    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('ficha_tecnica', views.ficha_tecnica, name="ficha_tecnica"),
    path('casa', views.casa, name="casa"),
    path('Cliente', views.clientes, name="Cliente"),
    path('casaFormulario', views.casaFormulario, name="Formulario de Casa"),
    path('fichaFormulario', views.fichaFormulario, name="Formulario de Ficha Tecnica"),
    path('clientesFormulario', views.clientesFormulario, name="Formulario de Clientes"), 
    
   ]

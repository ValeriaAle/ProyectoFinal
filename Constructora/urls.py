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
   
    path('busquedaCliente', views.busquedaclientes, name="BusquedaCliente"),
    path('buscar/', views.buscar),
    
    path('busquedaFicha', views.busquedaficha, name="BusquedaFicha"),
    path('buscar1/', views.buscar1),
    
    path('busquedaCasa', views.busquedacasa, name="BusquedaCasa"),
    path('buscar2/', views.buscar2),
    
   ]

from django.urls import path

from Constructora import views
from django.contrib.auth.views import LogoutView


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
    path('leerCli', views.leerClientes, name="leerClientes"),
    
    path('busquedaFicha', views.busquedaficha, name="BusquedaFicha"),
    path('buscar1/', views.buscar1),
    path('leerFichas', views.leerficha, name="leerFichas"),

    path('busquedaCasa', views.busquedacasa, name="BusquedaCasa"),
    path('buscar2/', views.buscar2),
    path('leercasas', views.leerCasa, name="leercasas"),
   
    path('casa/list', views.CasaList.as_view(), name='List1'),
    path(r'^(?P<pk>\d+)$' , views.CasaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CasaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CasaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CasaDelete.as_view(), name='Delete'),
        
    path('ficha/list', views.FichaList.as_view(), name='List2'),
    path(r'^(?P<pk>\w+)$' , views.FichaDetalle.as_view(), name='Detail2'),
    path(r'^nuevo$', views.FichaCreacion.as_view(), name='New2'),
    path(r'^editar/(?P<pk>\w+)$', views.FichaUpdate.as_view(), name='Edit2'),
    path(r'^borrar/(?P<pk>\w+)$', views.FichaDelete.as_view(), name='Delete2'),

    path('cliente/list', views.ClienteList.as_view(), name='List3'),
    path(r'^(?P<pk>\+)$' , views.ClienteDetalle.as_view(), name='Detail3'),
    path(r'^nuevo$', views.ClienteCreacion.as_view(), name='New3'),
    path(r'^editar/(?P<pk>\+)$', views.ClienteUpdate.as_view(), name='Edit3'),
    path(r'^borrar/(?P<pk>\+)$', views.ClienteDelete.as_view(), name='Delete3'),

    path('register', views.register, name='Register'),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='Constructora/logout.html'), name='Logout'),

   ]

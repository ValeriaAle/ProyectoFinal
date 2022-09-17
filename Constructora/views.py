from ast import Delete
from django.shortcuts import render, HttpResponse
from Constructora.models import Casa, cliente, Ficha_Tecnica



# Create your views here.
def inicio(request):

      return render(request, "Constructora/inicio.html")

def casa(request):

      return render(request, "Constructora/casa.html")

def clientes(request):

      return render(request, "Constructora/clientes.html")


def ficha_tecnica(request):

      return render(request, "Constructora/ficha_tecnica.html")

from Constructora.forms import CasaFormulario

def casaFormulario(request):

      if request.method == "POST":

            miFormulario = CasaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  inmueble  = Casa (numero=informacion["numero"], categoria=informacion["categoria"], domicilio=informacion["domicilio"], tipo=informacion["tipo"], fecha_disponible=informacion["fecha_disponible"], detalle=informacion["detalle"])
                  inmueble.save()
                  return render(request, "Constructora/inicio.html")

      else:
           miFormulario = CasaFormulario()

      return render(request, "Constructora/casaFormulario.html", {"miFormulario": miFormulario})

from Constructora.forms import FichaFormulario

def fichaFormulario(request):

      if request.method == "POST":

            miFormulario2 = FichaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario2)
            
            if miFormulario2.is_valid:
                  informacion = miFormulario2.cleaned_data
                  ficha_Tecnica = Ficha_Tecnica(obra=informacion["obra"], ubicacion=informacion["ubicacion"], superficie=informacion["superficie"], construccion=informacion["construccion"], plazos=informacion["plazos"])
                  ficha_Tecnica.save()
                  return render(request, "Constructora/inicio.html")

      else:
           miFormulario2 = FichaFormulario()

      return render(request, "Constructora/fichaFormulario.html", {"miFormulario": miFormulario2})

from Constructora.forms import ClientesFormulario

def clientesFormulario(request):

      if request.method == "POST":

            miFormulario3 = ClientesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario3)
            
            if miFormulario3.is_valid:
                  informacion = miFormulario3.cleaned_data
                  clientes_form = cliente(apellido_y_nombre=informacion["apellido_y_nombre"], referencia=informacion["referencia"], telefono=informacion["telefono"], domicilio_legal=informacion["domicilio_legal"])
                  clientes_form.save()
                  return render(request, "Constructora/inicio.html")

      else:
           miFormulario3 = ClientesFormulario()

      return render(request, "Constructora/clientesFormulario.html", {"miFormulario": miFormulario3})

def busquedaclientes(request):
      return render(request, "Constructora/busquedaClientes.html")      
def buscar(request):
      respuesta = f"Estoy buscando al Cliente: {request.GET['apellido_y_nombre']}"#No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def leerClientes(request):
      
      Cliente = cliente.objects.all()

      contexto= {"clientes": Cliente}

      return render(request, "Constructora/leerClientes.html",contexto)


def busquedaficha(request):
      return render(request, "Constructora/busquedaFicha.html")      
def buscar1(request):
      respuesta1 = f"Estoy buscando la ficha técnica: {request.GET['obra']}"#No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta1)
def leerficha(request):
      
      ficha = Ficha_Tecnica.objects.all()

      contexto2= {"fichas": ficha}

      return render(request, "Constructora/leerFicha.html",contexto2)
def eliminarFicha(request, ficha_obra):      
      ficha1 = Ficha_Tecnica.objects.get(obra=ficha_obra)
      ficha1.delete()
          

      casa2 = Casa.objects.all()
      contexto4= {"casas": casa2}
      return render(request, "Constructora/leerCasa.html",contexto4)



def busquedacasa(request):
      return render(request, "Constructora/busquedaCasa.html")      
def buscar2(request):
      respuesta2 = f"Estoy buscando la casa: {request.GET['numero']}"#No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta2)
def leerCasa(request):
      
      casa = Casa.objects.all()

      contexto3= {"casas": casa}

      return render(request, "Constructora/leerCasa.html",contexto3)

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CasaList(ListView):
      model = Casa
      template_name = "Constructora/casa_list.html"

class ClienteList(ListView):
      model = cliente
      template_name = "Constructora/cliente_list.html"

class FichaList(ListView):
      model = Ficha_Tecnica
      template_name = "Constructora/ficha_list.html"

class CasaDetalle(DetailView):
      model = Casa
      template_name = "Constructora/casa_detalle.html"

class ClienteDetalle(DetailView):
      model = cliente
      template_name = "Constructora/cliente_detalle.html"

class FichaDetalle(DetailView):
      model = Ficha_Tecnica
      template_name = "Constructora/ficha_detalle.html"

class CasaCreacion(CreateView):
      model = Casa
      success_url = "/Constructora/casa/list"
      fields = ['numero','categoria','domicilio','tipo','fecha_disponible', 'detalle']

class CasaUpdate (UpdateView):
      model = Casa
      success_url = "/Constructora/casa/list"
      fields = ['numero','categoria','domicilio','tipo','fecha_disponible', 'detalle']

class CasaDelete(DeleteView):
      model = Casa
      success_url = "/Constructora/casa/list"

class ClienteCreacion(CreateView):
      model = cliente
      success_url = "/Constructora/cliente/list"
      fields = ['apellido_y_nombre','referencia','telefono','domicilio_legal']

class ClienteUpdate (UpdateView):
      model = cliente
      success_url = "/Constructora/cliente/list"
      fields = ['apellido_y_nombre','referencia','telefono','domicilio_legal']

class ClienteDelete(DeleteView):
      model = cliente
      success_url = "/Constructora/cliente/list"

class FichaCreacion(CreateView):
      model = Ficha_Tecnica
      success_url = "/Constructora/ficha/list"
      fields = ['obra','ubicacion','superficie','construccion','plazos']

class FichaUpdate (UpdateView):
      model = Ficha_Tecnica
      success_url = "/Constructora/ficha/list"
      fields = ['obra','ubicacion','superficie','construccion','plazos']

class FichaDelete(DeleteView):
      model = Ficha_Tecnica
      success_url = "/Constructora/ficha/list"
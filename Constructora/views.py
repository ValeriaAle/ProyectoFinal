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
                  casa = Casa (numero=informacion["numero"], categoria=informacion["categoria"], domicilio=informacion["domicilio"], tipo=informacion["tipo"], fecha_disponible=informacion["fecha_disponible"],detalle=informacion["detalle"])
                  casa.save()
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



def busquedaficha(request):
      return render(request, "Constructora/busquedaFicha.html")      
def buscar1(request):
      respuesta1 = f"Estoy buscando la ficha técnica: {request.GET['obra']}"#No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta1)



def busquedacasa(request):
      return render(request, "Constructora/busquedaCasa.html")      
def buscar2(request):
      respuesta2 = f"Estoy buscando la casa: {request.GET['numero']}"#No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta2)

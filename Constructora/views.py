from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Constructora.models import cliente

# Create your views here.
def inicio(request):

      return render(request, "Constructora/inicio.html")

def casa(request):

      return render(request, "Constructora/casa.html")

def clientes(request):

      return render(request, "Constructora/clientes.html")


def ficha_tecnica(request):

      return render(request, "Constructora/ficha_tecnica.html")



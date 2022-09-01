from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Constructora.models import cliente

# Create your views here.
def inicio(request):

      return render(request, "Constructora/inicio.html")

def cursos(request):

      return render(request, "Constructora/cursos.html")

def clientes(request):

      return render(request, "Constructora/clientes.html")


def profesores(request):

      return render(request, "Constructora/profesores.html")



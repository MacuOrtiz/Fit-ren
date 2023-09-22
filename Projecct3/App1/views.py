from django.shortcuts import render
from django.http import HttpResponse
from .models import Prenda, Zapato, Accesorio

def inicio(request):
    return render(request, "App1/inicio.html")

def prendas(request):
    return render(request, "App1/prendas.html")

def zapatos(request):
    return render(request, "App1/zapatos.html")

def accesorios(request):
    return render(request, "App1/accesorios.html")

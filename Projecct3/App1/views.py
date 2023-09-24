from django.shortcuts import render
from django.http import HttpResponse
from .models import Prenda, Zapato, Accesorio, UserRegistro
from django.http import HttpResponseRedirect


def inicio(request):
    return render(request, "App1/inicio.html")

def prendas(request):
    return render(request, "App1/prendas.html")

def zapatos(request):
    return render(request, "App1/zapatos.html")

def accesorios(request):
    return render(request, "App1/accesorios.html")

def userRegistro(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        user_name = request.POST.get("userName")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip")

        user_registro = UserRegistro(
            firstName=first_name,
            lastName=last_name,
            userName=user_name,
            city=city,
            zip=zip_code
        )
        
        user_registro.save()
        
        return render(request, "App1/inicio.html")

    return render(request, "App1/userRegistro.html")

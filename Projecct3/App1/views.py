from django.shortcuts import render
from django.http import HttpResponse
from App1.forms import PrendaFormulario
from .models import UserRegistro, Prenda, Zapato
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

def login_requets(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("useName")  # Cambiado de "userName" a "username"
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje": f"Bienvenido {user}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "App1/login.html", {"formulario": form})

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
        password = request.POST.get("password")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip")

        user_registro = UserRegistro(
            firstName=first_name,
            lastName=last_name,
            userName=user_name,
            city=city,
            zip=zip_code,
            password=password
        )
        
        user_registro.save()
        
        return render(request, "App1/inicio.html")

    return render(request, "App1/userRegistro.html")

def buscarUsuario(request):
    return render(request, "App1/buscarUsuario.html")

def resultados(request):
    usuario = request.GET.get("usuario", "")  # Obtén el valor del parámetro 'usuario' de la URL
    userRegistro = UserRegistro.objects.filter(userName=usuario)
    
    if userRegistro.exists():  # Verifica si el usuario existe en la base de datos
        return render(request, 'App1/buscarUsuario.html', {'userRegistro': userRegistro, 'usuario': usuario})
    else:
        respuesta = "No existe el usuario"
        return HttpResponse(respuesta)

def leerPrendas(request):
    prendas = Prenda.objects.all()
    contexto = {"ropa": prendas}
    return render(request, "App1/leerPrendas.html", contexto)

def crearPrendas(request):
    if request.method == "POST":
        miFormulario = PrendaFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            nueva_prenda = Prenda(tipo=info["tipo"], costo=info["costo"], genero=info["genero"])
            nueva_prenda.save()
            return render(request, "App1/inicio.html") 
    else:
        miFormulario = PrendaFormulario()

    return render(request, "App1/prendaFormulario.html", {"miFormulario": miFormulario})  


def eliminarPrendas(request, predaTipo):
    prendas = Prenda.objects.filter(tipo=predaTipo)
    if prendas.exists():
        prenda = prendas.first()
        prenda.delete()
    predas = Prenda.objects.all()
    contexto = {"ropa": predas}
    return render(request, "App1/leerPrendas.html", contexto)


def editarPrendas(request, predaTipo):
    prenda = Prenda.objects.get(tipo=predaTipo)
    if request.method == "POST":
     miFormulario = PrendaFormulario(request.POST)

     if miFormulario.is_valid():
            info = miFormulario.cleaned_data

            prenda.tipo=info["tipo"]
            prenda.costo=info["costo"]
            prenda.genero=info["genero"]
            prenda.save()

            return render(request, "App1/inicio.html") 
    else:
        miFormulario = PrendaFormulario(initial={"tipo": prenda.tipo, "costo":prenda.costo, "genero":prenda.genero})

    return render(request, "App1/editarPrendas.html", {"miFormulario": miFormulario, "nombre":predaTipo}) 


class ListaZapato(ListView):
    model=Zapato

class DetalleZapato(DetailView):
    model=Zapato

class CrearZapato(CreateView):
    model=Zapato
    success_url = "/App/zapatos/list"
    fields = ["estilo", "costo", "genero", "imagen_url"]

class ActualizarZapato (UpdateView):
    model=Zapato
    success_url = "/App/zapatos/list"
    fields = ["estilo", "costo", "genero", "imagen_url"]  

class BorrarZapato(DeleteView):
    model=Zapato
    success_url = "/App/zapatos/lista"
    
        
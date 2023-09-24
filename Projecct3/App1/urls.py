from django.urls import path
from App1.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('prendas/', prendas, name="Prendas"),
    path('zapatos/', zapatos, name="Zapatos"),
    path('accesorios/', accesorios, name="Accesorios"),
    path('userRegistro/', userRegistro, name="RegistroUser"),  
]


from django.urls import path
from App1.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('prendas/', prendas, name="Prendas"),
    path('zapatos/', zapatos, name="Zapatos"),
    path('accesorios/', accesorios, name="Accesorios"),
    path('userRegistro/', userRegistro, name="RegistroUser"), 
    path("buscarUsuario/", buscarUsuario, name="BusquedaUsuario"), 
    path("resultados/", resultados, name='Resultados'), 
    
    #crud prendas
    path("zapatos/list", leerPrendas, name='RopaLeer'), 
    path("creearPrenda/", crearPrendas, name='RopaCrear'), 
    path("eliminarPrendas/<predaTipo>", eliminarPrendas, name='PrendaEliminar'),
    path("editarPrendas/<predaTipo>", editarPrendas, name='PrendaEditar'),

     #crud zapatos
    path("zapatos/lista/", ListaZapato.as_view(), name='ZapatosLeer'),
    path("zapatos/detalle/<int:pk>/", DetalleZapato.as_view(), name='ZapatosDetalle'), 
]



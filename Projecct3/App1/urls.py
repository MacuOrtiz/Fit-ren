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
    path("login/", login_requets, name='Login'), 

    
    #crud prendas
    path("zapatos/list", leerPrendas, name='RopaLeer'), 
    path("creearPrenda/", crearPrendas, name='RopaCrear'), 
    path("eliminarPrendas/<predaTipo>", eliminarPrendas, name='PrendaEliminar'),
    path("editarPrendas/<predaTipo>", editarPrendas, name='PrendaEditar'),

     #crud zapatos
    path("zapatos/lista/", ListaZapato.as_view(), name='ZapatosLeer'),
    path("zapatos/detalle/<int:pk>/", DetalleZapato.as_view(), name='ZapatosDetalle'),
    path("zapatos/crear/", CrearZapato.as_view(), name='ZapatosCrear'),  
    path("zapatos/editar/<int:pk>/", ActualizarZapato.as_view(), name='ZapatosEditar'),
    path("zapatos/borrar/<int:pk>/", BorrarZapato.as_view(), name='ZapatosBorrar'),
]



from django.urls import path
from App1.views import *

urlpatterns = [
    
    path('inicio/', inicio),
    path('prendas/', prendas),
    path('zapatos/', zapatos),
    path('accesorios/', accesorios),
]
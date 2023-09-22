
from django.db import models

class Prenda(models.Model):
    tipo = models.CharField(max_length=20)
    costo = models.IntegerField()
    genero = models.CharField(max_length=10)

class Zapato(models.Model):
    estilo = models.CharField(max_length=20)
    costo = models.IntegerField()
    genero = models.CharField(max_length=10)

class Accesorio(models.Model):
    categoria = models.CharField(max_length=20)
    costo = models.IntegerField()
    genero = models.CharField(max_length=10)
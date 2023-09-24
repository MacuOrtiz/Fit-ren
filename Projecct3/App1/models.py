
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

class UserRegistro(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    userName=models.CharField(max_length=8)
    city=models.CharField(max_length=20)
    zip=models.IntegerField()


    
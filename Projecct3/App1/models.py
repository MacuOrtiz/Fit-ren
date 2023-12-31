from django.db import models
from django.contrib.auth.hashers import make_password  

class Prenda(models.Model):
    tipo = models.CharField(max_length=20)
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=50.25)
    genero = models.CharField(max_length=10)
    imagen_url = models.URLField(blank=True, null=True)  # Campo para la URL de la imagen

    def __str__(self):
        return f"Tipo: {self.tipo} -- Costo: {self.costo} -- Genero: {self.genero}"


class Zapato(models.Model):
    estilo = models.CharField(max_length=20)
    costo = models.IntegerField()
    genero = models.CharField(max_length=10)
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Estilo: {self.estilo} -- Costo: {self.costo} -- Genero: {self.genero}"


class Accesorio(models.Model):
    
    def __str__(self):
        return f"Categoria: {self.categoria } -- Costo:{self.costo} -- Genero:{self.genero}"
    
    categoria = models.CharField(max_length=20)
    costo = models.IntegerField()
    genero = models.CharField(max_length=10)
    imagen_url = models.URLField(blank=True, null=True)

class UserRegistro(models.Model):
    
    def __str__(self):
        return f"FirstName: {self.firstName} -- LastName:{self.lastName} -- UserName:{self.userName} -- City:{self.city} -- Zip:{self.zip}"

    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    userName=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zip=models.IntegerField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # cifra la contraseña antes de guardarla
        super().save(*args, **kwargs)



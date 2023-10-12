from django.db import models

class Prenda(models.Model):
    tipo = models.CharField(max_length=20)
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=50.25)
    genero = models.CharField(max_length=10)
    imagen_url = models.URLField(blank=True, null=True)  # Campo para la URL de la imagen

    def __str__(self):
        return f"Tipo: {self.tipo} -- Costo: {self.costo} -- Genero: {self.genero}"



class Zapato(models.Model):

    def __str__(self):
        return f"Estilo: {self.estilo } -- Costo:{self.costo} -- Genero:{self.genero}"
    
    estilo = models.CharField(max_length=20)
    costo = models.IntegerField()
    genero = models.CharField(max_length=10)
    imagen_url = models.URLField(blank=True, null=True)

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
    userName=models.CharField(max_length=8)
    city=models.CharField(max_length=20)
    zip=models.IntegerField()



from django.db import models
from django.urls import reverse

class Director(models.Model):
    nombre     = models.CharField(max_length=30)
    apellidos  = models.CharField(max_length=50)
    nacimiento = models.DateField()
    defuncion  = models.DateField(null= True, blank = True)
    premios    = models.TextField(default="No tiene premios")

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def get_absolute_url(self):
        return

class Pelicula(models.Model):
    titulo   = models.CharField(max_length=30)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null= True, blank=True)
    sinopsis = models.TextField()
    estreno  = models.IntegerField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("Pelicula", kwargs={"id": self.id})
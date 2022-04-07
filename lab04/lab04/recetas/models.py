import email
from tabnanny import verbose
from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=200)
    email=models.EmailField()
    def __str__(self):
        return self.nombre
class Receta(models.Model):
    titulo=models.CharField(max_length=100,unique=True)
    ingredientes=models.TextField(help_text='Escribe los ingredientes')
    preparacion=models.TextField()
    tiempo_registro=models.DateTimeField(auto_now=True)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
class Comentario(models.Model):
    receta=models.ForeignKey(Receta, on_delete=models.CASCADE)
    text=models.TextField(help_text='Escribe tu comentario',verbose_name='Comentario')
    def __str__(self):
        return self.text
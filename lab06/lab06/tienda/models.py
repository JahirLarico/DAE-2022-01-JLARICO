from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from unicodedata import decimal
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre  = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=40)
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre
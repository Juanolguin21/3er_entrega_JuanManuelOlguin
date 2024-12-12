from django.db import models

# Create your models here.
class neoprenos(models.Model) :
    marca =models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    serie=models.IntegerField()
    
class cliente(models.Model) :
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    direccion=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    
class sucursal(models.Model):
    nombre=models.CharField(max_length=30)
    pais=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    
class pedido(models.Model):
    cantidad=models.IntegerField()
    fechapedido=models.DateField()
    entregado=models.BooleanField()
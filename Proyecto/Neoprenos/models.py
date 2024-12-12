from django.db import models

# Create your models here.
class neoprenos(models.Model) :
    marca =models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    serie=models.IntegerField()
    tipo=models.CharField(max_length=20)
    def __str__(self):
        return f"Marca: {self.marca}  | Modelo:{self.modelo} | Medida:{self.serie} | Tipo:{self.tipo}"
    
class cliente(models.Model) :
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    direccion=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre}  | Apellido:{self.apellido} | Email:{self.email} | Direccion:{self.direccion} | Telefono:{self.telefono}"
    
class sucursal(models.Model):
    nombre=models.CharField(max_length=30)
    pais=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre}  | Pais:{self.pais} | telefono:{self.telefono} | direccion:{self.direccion} | email:{self.email}"
    
class pedido(models.Model):
    cantidad=models.IntegerField()
    fechapedido=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"Cantidad: {self.cantidad}  | Fecha pedido:{self.fechapedido} | Entregado:{self.entregado}"
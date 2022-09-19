from readline import append_history_file
from django.db import models

# Create your models here.

class empleados(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField()
    dni=models.integer_field()
    cuil=models.integer_field()
    wwid=models.integer_field()
    sector=models.CharField(max_length=20)
    antiguedad=models.DateField()
    direccion=models.CharField(max_length=50)
    telefono=models.integer_field()
    email=models.EmailField()
    art=models.CharField(max_length=30)
    cbu=models.integer_field()
    estado=models.BooleanField()

class tercerizados(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField()
    dni=models.integer_field()
    cuil=models.integer_field()
    empresa=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    art=models.CharField(max_length=30)

class clientes(models.Model):
    razon_social=models.CharField(max_length=30)
    cuit=models.integer_field()
    direccion=models.CharField(max_length=50)
    telefono=models.integer_field()
    email=models.EmailField()

class clientesparticulares(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.integer_field()
    direccion=models.CharField(max_length=50)
    telefono=models.integer_field()
    email=models.EmailField()

class proveedores(models.Model):
    razon_social=models.CharField(max_length=30)
    cuit=models.integer_field()
    direccion=models.CharField(max_length=50)
    telefono=models.integer_field()
    email=models.EmailField()
    cbu=models.integer_field()




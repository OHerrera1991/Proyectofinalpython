from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField()
    dni=models.IntegerField()
    cuil=models.IntegerField()
    wwid=models.IntegerField()
    sector=models.CharField(max_length=20)
    antiguedad=models.DateField()
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    art=models.CharField(max_length=30)
    cbu=models.IntegerField()

class Tercerizados(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField()
    dni=models.IntegerField()
    cuil=models.IntegerField()
    empresa=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    art=models.CharField(max_length=30)

class Clientes(models.Model):
    razon_social=models.CharField(max_length=30)
    cuit=models.IntegerField()
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

class ClientesParticulares(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

class Proveedores(models.Model):
    razon_social=models.CharField(max_length=30)
    cuit=models.IntegerField()
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    cbu=models.IntegerField()




from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Empleados)
admin.site.register(Tercerizados)
admin.site.register(Clientes)
admin.site.register(ClientesParticulares)
admin.site.register(Proveedores)
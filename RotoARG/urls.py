from unittest.mock import patch
from django.urls import path
from django.views import *
from RotoARG.views import *

urlpatterns = [
    path('', index),
    path('empleados/', empleados),
    path('tercerizados/', empleados_tercerizados),
    path('proveedores/', proveedores),
    path('clientes/', clientes ),
    path('particulares/', particulares),
    path('buscar_cliente/', buscar_cliente),
    path('buscar_empleado/', buscar_empleado),
    path('buscar_tercerizado/', buscar_tercerizado),
    path('buscar_proveedor/', buscar_proveedor),

    path('buscar_clientes_particulares/', buscar_clientes_particulares),


]
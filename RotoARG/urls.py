from unittest.mock import patch
from django.urls import path
from django.views import *
from RotoARG.views import *

urlpatterns = [
    path('', index),
    path('empleados/', empleados),
<<<<<<< HEAD
    path('tercerizados/', tercerizados),
=======
    path('tercerizados/', empleados_tercerizados),
>>>>>>> d2a2ff4301b06a713aad5956974ad8602a61b404
    path('proveedores/', proveedores),
    path('clientes/', clientes ),
    path('particulares/', clientes_particulares),
    path('buscar_cliente/', buscar_cliente),
<<<<<<< HEAD
    path('buscar_empleado/', buscar_empleado),
    path('buscar_tercerizado/', buscar_tercerizado),
    path('buscar_proveedor/', buscar_proveedor),
    path('buscar_clientes_particulares/', buscar_clientes_particulares),
=======
>>>>>>> d2a2ff4301b06a713aad5956974ad8602a61b404
]
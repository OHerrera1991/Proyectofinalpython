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
    path('particulares/', clientes_particulares),
    path('buscar_cliente/', buscar_cliente),
]
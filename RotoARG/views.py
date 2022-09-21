from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def empleados(request):
    return render(request, "personal.html")

def empleados_tercerizados(request):
    return render(request, "tercerizados.html")

def proveedores(request):
    return render(request, "proveedores.html")

def clientes(request):
    return render(request, "clientes.html")

def clientes_particulares(request):
    return render(request, "particulares.html")

import email
from django.shortcuts import render
from django.http import HttpResponse
from RotoARG.models import Clientes
from RotoARG.forms import form_clientes

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
    if request.method == "POST":
        cliente = Clientes(razon_social = request.POST["razonsocial"], cuit= request.POST["cuit"], direccion =request.POST["direccion"], telefono =request.POST["telefono"], email= request.POST["email"])
        cliente.save()
        return render(request, "index.html")
    return render(request,"clientes.html")

def buscar_cliente(request):
    if request.GET["email"]:
        email = request.GET["email"]
        clientes = Clientes.objects.filter(email__icontains=email)
        return render(request, "clientes.html", {"clientes": clientes})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)

def clientes_particulares(request):
    return render(request, "particulares.html")

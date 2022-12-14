import email
from django.shortcuts import render
from django.http import HttpResponse
from RotoARG.models import *
from RotoARG.forms import form_clientes

# Create your views here.

def index(request):
    return render(request, "index.html")

##EMPLEADOS##
def empleados(request):
    if request.method == "POST":
        empleado = Empleados(nombre = request.POST["nombre"], apellido= request.POST["apellido"], fecha_nacimiento= request.POST["fechanacimiento"], dni= request.POST["dni"], cuil= request.POST["cuil"], wwid= request.POST["wwid"], sector= request.POST["sector"], antiguedad= request.POST["antiguedad"], direccion =request.POST["direccion"], telefono =request.POST["telefono"], email= request.POST["email"], art= request.POST["art"], cbu= request.POST["cbu"],)
        empleado.save()
        return render(request, "index.html")
    return render(request,"personal.html")

def buscar_empleado(request):
    if request.GET["dni"]:
        dni = request.GET["dni"]
        empleados = Empleados.objects.filter(dni__icontains=dni)
        return render(request, "personal.html", {"empleados": empleados})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)


##EMPLEADOS TERCERIZADOS##
def tercerizados(request):
    if request.method == "POST":
        tercerizado = Tercerizados(nombre = request.POST["nombre"], apellido= request.POST["apellido"], fecha_nacimiento= request.POST["fechanacimiento"], dni= request.POST["dni"], cuil= request.POST["cuil"], empresa= request.POST["empresa"], area= request.POST["area"], art= request.POST["art"])
        tercerizado.save()
        return render(request, "index.html")
    return render(request,"tercerizados.html")

def buscar_tercerizado(request):
    if request.GET["dni"]:
        dni = request.GET["dni"]
        tercerizados = Tercerizados.objects.filter(dni__icontains=dni)
        return render(request, "tercerizados.html", {"tercerizados": tercerizados})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

##PROVEEDORES##
def proveedores(request):
    if request.method == "POST":
        proveedor = Proveedores(razon_social = request.POST["razonsocial"], cuit= request.POST["cuit"], direccion =request.POST["direccion"], telefono =request.POST["telefono"], email= request.POST["email"], cbu =request.POST["cbu"])
        proveedor.save()
        return render(request, "index.html")
    return render(request,"proveedores.html")

def buscar_proveedor(request):
    if request.GET["email"]:
        email = request.GET["email"]
        proveedores = Proveedores.objects.filter(email__icontains=email)
        return render(request, "proveedores.html", {"proveedores": proveedores})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

##CLIENTES##
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

def buscar_cliente(request):
    if request.GET["email"]:
        email = request.GET["email"]
        clientes = Clientes.objects.filter(email__icontains=email)
        return render(request, "clientes.html", {"clientes": clientes})
    else:
        respuesta = "no enviaste datos"
    return HttpResponse(respuesta)

##CLIENTES PARTICULARES##
def particulares(request):
    if request.method == "POST":
        particular = ClientesParticulares(nombre = request.POST["nombre"], apellido= request.POST["apellido"], dni= request.POST["dni"], direccion =request.POST["direccion"], telefono =request.POST["telefono"], email= request.POST["email"])
        particular.save()
        return render(request, "index.html")
    return render(request,"particulares.html")

def buscar_particulares(request):
    if request.GET["email"]:
        email = request.GET["email"]
        particulares = ClientesParticulares.objects.filter(email__icontains=email)
        return render(request, "particulares.html", {"particulares": particulares})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

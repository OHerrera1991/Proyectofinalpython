from django import forms

class form_clientes(forms.Form):
    razon_social=forms.CharField(max_length=30)
    cuit=forms.IntegerField()
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    email=forms.EmailField()
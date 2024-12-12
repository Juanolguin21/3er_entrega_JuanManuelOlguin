from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request): 
    return render (request, "Neoprenos/inicio.html")

def trajes(request): 
    return render (request, "Neoprenos/trajes.html")

def login(request): 
    return render (request, "Neoprenos/login.html")

def tienda(request): 
    return render (request, "Neoprenos/tienda.html")

def contacto(request): 
    return render (request, "Neoprenos/contacto.html")

def sucursales(request): 
    return render (request, "Neoprenos/sucursales.html")
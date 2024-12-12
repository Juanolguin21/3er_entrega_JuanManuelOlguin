from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request): 
    return render (request, "Neoprenos/inicio.html")

def trajes(request): 
    return render (request, "Neoprenos/trajes.html")

def loguin(request): 
    return render (request, "Neoprenos/loguin.html")

def pedidos(request): 
    return render (request, "Neoprenos/pedidos.html")

def sucursales(request): 
    return render (request, "Neoprenos/sucursales.html")
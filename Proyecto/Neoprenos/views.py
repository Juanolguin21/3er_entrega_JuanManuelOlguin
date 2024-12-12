from django.shortcuts import render
from django.http import HttpResponse
from Neoprenos.models import neoprenos
from .forms import BuscarProductoForm

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


def neoprenos_Formulario(request):
      if request.method == 'POST':
      
            Neoprenos = neoprenos(marca=request.POST['marca'],modelo=request.POST['modelo'],serie=request.POST['serie'],tipo=request.POST['tipo'])
 
            Neoprenos.save()
 
            return render(request, "Neoprenos/inicio.html")
 
      return render(request,"Neoprenos/neoprenos_Formulario.html")
  
def buscar_producto(request):
    form = BuscarProductoForm()
    resultados = None

    if 'query' in request.GET:
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = neoprenos.objects.filter(marca__icontains=query)

    return render(request, 'Neoprenos/buscar_producto.html', {'form': form, 'resultados': resultados})
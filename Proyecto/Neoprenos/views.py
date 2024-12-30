from django.shortcuts import render
from django.http import HttpResponse
from Neoprenos.models import neoprenos
from .forms import BuscarProductoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import neoprenos  # Asegúrate de importar tu modelo
from .forms import AltaProductoForm, ModificacionProductoForm



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


@login_required
def neoprenos_Formulario(request):
      if request.method == 'POST':
      
            Neoprenos = neoprenos(marca=request.POST['marca'],modelo=request.POST['modelo'],serie=request.POST['serie'],tipo=request.POST['tipo'])
 
            Neoprenos.save()
 
            return render(request, "Neoprenos/inicio.html")
 
      return render(request,"Neoprenos/neoprenos_Formulario.html")
  
  
@login_required
def buscar_producto(request):
    form = BuscarProductoForm()
    resultados = None

    if 'query' in request.GET:
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = neoprenos.objects.filter(marca__icontains=query)

    return render(request, 'Neoprenos/buscar_producto.html', {'form': form, 'resultados': resultados})


# Vista para el Alta
def alta_producto(request):
    if request.method == 'POST':
        form = AltaProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar_producto')
    else:
        form = AltaProductoForm()
    return render(request, 'Neoprenos/alta_producto.html', {'form': form})

# Vista para la Baja
def baja_producto(request, id):
    item = get_object_or_404(neoprenos, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('buscar_producto')
    return render(request, 'Neoprenos/baja_producto.html', {'item': item})

# Vista para la Modificación
def modificacion_producto(request, id):
    item = get_object_or_404(neoprenos, id=id)
    if request.method == 'POST':
        form = ModificacionProductoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('buscar_producto')
    else:
        form = ModificacionProductoForm(instance=item)
    return render(request, 'Neoprenos/modificacion_producto.html', {'form': form, 'item': item})






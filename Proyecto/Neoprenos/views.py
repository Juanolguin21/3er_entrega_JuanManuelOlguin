from django.shortcuts import render
from django.http import HttpResponse
from Neoprenos.models import neoprenos
from .forms import BuscarProductoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import neoprenos  
from .forms import AltaProductoForm, ModificacionProductoForm
from django.contrib import messages


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

def portfolio(request): 
    return render (request, "Neoprenos/portfolio.html")


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

@login_required
def modificar_producto(request, producto_id):
    producto = get_object_or_404(neoprenos, id=producto_id)

    if request.method == 'POST':
        form = ModificacionProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto modificado correctamente.")
            return redirect('gestionarProducto') 
    else:
        form = ModificacionProductoForm(instance=producto)

    return render(request, 'Neoprenos/modificar_producto.html', {'form': form, 'producto': producto})


@login_required
def gestionar_Producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')  
        accion = request.POST.get('accion') 

        if accion == 'baja':
            try:
                producto = get_object_or_404(neoprenos, id=producto_id)  
                producto.delete()
                messages.success(request, "Producto eliminado correctamente.")
            except:
                messages.error(request, "Error: El producto con ID proporcionado no existe.")
            return redirect('gestionarProducto') 

        elif accion == 'modificacion':
            try:
                producto = get_object_or_404(neoprenos, id=producto_id)
                return redirect('modificar_producto', producto_id=producto_id)  
            except Exception as e:
                messages.error(request, "Error: El ID del producto no es válido.")
                return redirect('gestionarProducto')  
        
    return render(request, "Neoprenos/gestionar_Producto.html")






from django.urls import path
from Neoprenos import views
from . import views
from .views import buscar_producto, gestionar_Producto, modificar_producto



urlpatterns = [
      path('inicio/', views.inicio, name='Inicio'),
      path('trajes/', views.trajes,name='Trajes'),
      path('login/', views.login,name='Login'),
      path('tienda/', views.tienda,name='Tienda'),
      path('contacto/', views.contacto,name='Contacto'),
      path('sucursales/', views.sucursales,name='Sucursales'),
      path('buscar-producto/', views.buscar_producto, name='buscar')

      
]

forms_html= [
    path('neoprenos-Formulario/', views.neoprenos_Formulario, name="neoprenosFormulario"),
    path('gestionar-Producto/', views.gestionar_Producto, name='gestionarProducto'),
    path('modificar_producto/<int:producto_id>/', modificar_producto, name='modificar_producto')
]

urlpatterns += forms_html

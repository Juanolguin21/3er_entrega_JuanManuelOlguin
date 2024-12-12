
from django.urls import path
from Neoprenos import views
from . import views


urlpatterns = [
      path('inicio/', views.inicio, name='Inicio'),
      path('trajes/', views.trajes,name='Trajes'),
      path('login/', views.login,name='Login'),
      path('tienda/', views.tienda,name='Tienda'),
      path('contacto/', views.contacto,name='Contacto'),
      path('sucursales/', views.sucursales,name='Sucursales')
      
]

forms_html= [
    path('neoprenos-Formulario/', views.neoprenos_Formulario, name="neoprenosFormulario"),
    path('buscar-producto/', views.buscar_producto, name='buscar')
]

urlpatterns += forms_html

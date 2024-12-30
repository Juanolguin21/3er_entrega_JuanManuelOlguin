
from django.urls import path
from Neoprenos import views
from . import views
from .views import buscar_producto, alta_producto, baja_producto, modificacion_producto



urlpatterns = [
      path('inicio/', views.inicio, name='Inicio'),
      path('trajes/', views.trajes,name='Trajes'),
      path('login/', views.login,name='Login'),
      path('tienda/', views.tienda,name='Tienda'),
      path('contacto/', views.contacto,name='Contacto'),
      path('sucursales/', views.sucursales,name='Sucursales'),
      path('buscar/', buscar_producto, name='buscar_producto'),
      path('alta/', alta_producto, name='alta_producto'),
      path('baja/<int:id>/', baja_producto, name='baja_producto'),
      path('modificacion/<int:id>/', modificacion_producto, name='modificacion_producto'),
     
      
]

forms_html= [
    path('neoprenos-Formulario/', views.neoprenos_Formulario, name="neoprenosFormulario"),
    path('buscar-producto/', views.buscar_producto, name='buscar')
]

urlpatterns += forms_html


from django.urls import path
from Neoprenos import views

urlpatterns = [
      path('inicio/', views.inicio, name='Inicio'),
      path('trajes/', views.trajes,name='Trajes'),
      path('login/', views.login,name='Login'),
      path('tienda/', views.tienda,name='Tienda'),
      path('contacto/', views.contacto,name='Contacto'),
      path('sucursales/', views.sucursales,name='Sucursales')
]

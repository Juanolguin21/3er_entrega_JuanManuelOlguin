
from django.urls import path
from Neoprenos import views

urlpatterns = [
      path('inicio/', views.inicio),
      path('trajes/', views.trajes),
      path('login/', views.login),
      path('tienda/', views.tienda),
      path('contacto/', views.contacto),
      path('sucursales/', views.sucursales)
]

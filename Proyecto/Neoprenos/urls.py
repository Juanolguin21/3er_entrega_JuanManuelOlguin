
from django.urls import path
from Neoprenos import views

urlpatterns = [
      path('inicio/', views.inicio),
      path('trajes/', views.trajes),
      path('loguin/', views.loguin),
      path('pedidos/', views.pedidos),
      path('sucursales/', views.sucursales)
     
]

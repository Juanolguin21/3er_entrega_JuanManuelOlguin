from django.contrib import admin
from Neoprenos.models import neoprenos,pedido,cliente,sucursal
# Register your models here.


admin.site.register(neoprenos)

admin.site.register(pedido)

admin.site.register(sucursal)

admin.site.register(cliente)
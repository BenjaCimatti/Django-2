from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['RUT','nombre','telefono']
    list_display = ['RUT','nombre','telefono']
    list_display_links = ['RUT','nombre','telefono']

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Detalle)

from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['RUT','nombre','telefono']
    list_display = ['RUT','nombre','telefono']
    list_display_links = ['RUT','nombre','telefono']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','proveedor','precio','stock']
    list_display_links = ['nombre','proveedor','precio','stock']
    fieldsets = (
        ("Descripcion", {
            'fields':('nombre','categoria','proveedor',)
        }),
        ('Variables', {
            'fields':('precio','stock',)
        }),
    )

class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['nombre','RUT']
    list_display = ['nombre','telefono','direccion']
    list_display_links = ['nombre','telefono','direccion']

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle)

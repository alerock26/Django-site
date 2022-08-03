from django.contrib import admin
from .models import CatProducto, Producto

# Register your models here.

class CatProductoAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    read_only_fields = ('created', 'updated')

admin.site.register(CatProducto, CatProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
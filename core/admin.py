from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 5
    list_filter = ['tipo']
    list_editable = ['precio','stock','descripcion','tipo']

admin.site.register(Producto,ProductoAdmin)
admin.site.register(TipoProducto)
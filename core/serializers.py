# SE VA A ENCARGAR DE CONVERTIR LOS ARCHIVOS A JSON
from .models import *
from rest_framework import serializers

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    # AGREGAR LAS FK
    tipo = TipoProductoSerializer(read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'

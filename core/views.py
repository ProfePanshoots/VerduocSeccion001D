from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import *
import requests

# Create your views here.
## VIEWS - URLS - HTML

# VIEWSET QUE SE ENCARGA DE TRANSFORMAR LA DATA
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoProductoViewset(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer


# LISTO LOS PRODUCTOS EN INDEX
def index(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto
    
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 5)
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'listado': productosAll,
        'paginator': paginator
    }

    return render(request, 'core/index.html', data)

def indexapi(request):
    # REALIZAMOS UNA SOLICITUD AL API
    response = requests.get('http://127.0.0.1:8000/api/productos/')
    response2 = requests.get('https://mindicador.cl/api/')
    response3 = requests.get('https://rickandmortyapi.com/api/character/')

    # TRANSFORMA EL JSON PARA LEERLO
    productos = response.json()
    monedas = response2.json()
    aux = response3.json()
    personajes = aux['results']

    data = {
        'listado': productos,
        'moneda' : monedas,
        'personajes': personajes,
    } 

    return render(request, 'core/indexapi.html', data)


#CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # CAPTURAMOS LA INFO DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # INSERT INTO producto VALUES()
            #data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add-product.html', data)

def update(request, id):
    producto = Producto.objects.get(id=id) # SELECT CON WHERE (BUSCAR)
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() # INSERT INTO producto VALUES()
            #data['msj'] = "Producto modificado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario # MOSTRAR EN LA VISTA LOS CAMBIOS

    return render(request, 'core/update-product.html', data)

def delete(request, id):
    producto = Producto.objects.get(id=id) # SELECT CON WHERE (BUSCAR)
    producto.delete()

    return redirect(to="index")

def cart(request):
    response = requests.get('https://mindicador.cl/api/dolar')
    moneda = response.json()
    valor_dolar = moneda['serie'][0]['valor'] # VALOR DEL DOLAR ACTUAL
    total_carrito = 15000 # ACA SE SUPONE QUE SUMAN LOS PRECIOS DEL CARRITO
    valor = total_carrito/valor_dolar # PRECIO TRANSFORMADO A DOLAR
    valor = round(valor, 2) # LO REDONDEO A DOS DECIMALES
    data = {
        'valor' : valor
    }  

    return render(request, 'core/cart.html', data)

def about(request):
    return render(request, ('core/about.html'))

def blog(request):
    return render(request, ('core/blog.html'))

def blogsingle(request):
    return render(request, ('core/blog-single.html'))

def checkout(request):
    return render(request, ('core/checkout.html'))

def contact(request):
    return render(request, ('core/contact.html'))

def productsingle(request):
    return render(request, ('core/product-single.html'))

@login_required
def shop(request):
    return render(request, ('core/shop.html'))

def wishlist(request):
    return render(request, ('core/wishlist.html'))
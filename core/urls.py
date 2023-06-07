## VIEWS - URLS - HTML
from django.urls import path, include
from .views import *
from rest_framework import routers

# PARA CREAR EL API
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipo_productos', TipoProductoViewset)

urlpatterns = [
    path('', index, name="index"),
    path('indexapi', indexapi, name="indexapi"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('blogsingle/', blogsingle, name="blogsingle"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('contact/', contact, name="contact"),
    path('productsingle/', productsingle, name="productsingle"),
    path('shop/', shop, name="shop"),
    path('wishlist/', wishlist, name="wishlist"),
    # CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    # API
    path('api/', include(router.urls)),
]
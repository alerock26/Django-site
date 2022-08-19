from django.shortcuts import render, redirect
from .cart import Carro
from apps.tienda.models import Producto

# Create your views here.

def add_product(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('tienda_home_view')

def delete_product(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('tienda_home_view')

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('tienda_home_view')

def clear_cart(request):
    carro = Carro(request)
    carro.clear_cart()
    return redirect('tienda_home_view')
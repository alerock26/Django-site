from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda_home_view(request):
    all_products = Producto.objects.all()
    return render(request, 'tienda/home_tienda_view.html', {'productos':all_products})
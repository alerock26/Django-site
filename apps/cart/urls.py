from django.urls import path
from .views import add_product

app_name = 'carro'

urlpattern = [
    path('agregar_producto/<int:producto_id>', add_product, name='agregar_producto')
]
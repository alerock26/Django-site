from django.urls import path
from .views import add_product, restar_producto

app_name = 'carro'

urlpatterns = [
    path('agregar_producto/<int:producto_id>', add_product, name='agregar_producto'),
    path('restar_producto/<int:producto_id>', restar_producto, name='restar_producto'),
]
from django.urls import path
from .views import tienda_home_view

urlpatterns = [
    path('', tienda_home_view, name='tienda_home_view'),
]
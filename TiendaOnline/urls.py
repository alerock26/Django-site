"""TiendaOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Link to apps/core.urls
    path('', include('apps.core.urls')),

    path('servicios/' , include('apps.servicios.urls')),

    path('blog/', include('apps.blog.urls')),

    path('tienda/', include('apps.tienda.urls')),

    path('contacto/', include('apps.contacto.urls')),

    path('carro/', include('apps.cart.urls')),

    path('user/', include('apps.autenticacion.urls')),
]

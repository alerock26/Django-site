from django.shortcuts import render
from .models import Servicio
# Create your views here.

def servicios_view(request):
    all_services = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {'all_services':all_services})
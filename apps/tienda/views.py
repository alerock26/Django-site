from django.shortcuts import render

# Create your views here.

def tienda_home_view(request):
    return render(request, 'tienda/home_tienda_view.html')
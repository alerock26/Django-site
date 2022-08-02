from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    return render(request, 'core/contact_view.html')
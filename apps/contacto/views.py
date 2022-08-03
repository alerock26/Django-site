from django.shortcuts import render, redirect
from .forms import contact_form
from django.core.mail import EmailMessage

# Create your views here.

def contact_view(request):
    contact = contact_form()
    if request.method == 'POST':
        contact = contact_form(data=request.POST)
        if contact.is_valid():
            nombre = request.POST.get('nombre')
            correo = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            print(f'''Gracias por contactarnos {nombre}, su email: {correo} quedara en 
            nuestra base de datos, gracias por su mensaje: "{mensaje[:10]}"''')
            return redirect('/contacto/?valid')
    elif request.method == 'GET':
        return render(request, 'contacto/contact_view.html', {'form':contact})
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form':form}) 

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home_view')
        else:
            for i in form.error_messages:
                messages.error(request, form.error_messages[i])

            return render(request, 'registro/registro.html', {'form':form}) 

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password')
            usser = authenticate(username=user_name, password=passwd)
            if usser is not None:
                login(request, usser)
                return redirect('home_view')
            else:
                messages.error(request, 'authentication error')
        else:
            messages.error(request, 'auth error')
    form = AuthenticationForm()
    return render(request, 'registro/login.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home_view')
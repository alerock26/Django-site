from django.urls import path
from .views import VRegistro, cerrar_sesion, user_login

app_name='apps.autenticacion'

urlpatterns = [
    path('', VRegistro.as_view(), name='user_home'),
    path('cerrar_session', cerrar_sesion, name='cerrar_sesion'),
    path('user_login', user_login, name='user_login'),
]
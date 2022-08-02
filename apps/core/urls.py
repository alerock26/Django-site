from django.urls import path
from .views import home_view, contact_view

# Para agregar las url de ficheros MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home_view' ),
    #path('servicios', servicios_view, name='servicios_view'),

    path('contact', contact_view, name='contact_view'),
]

# Agrega la URL de MEDIA files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

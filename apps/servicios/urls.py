from django.urls import path
from .views import servicios_view

# Para agregar las url de ficheros MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', servicios_view, name='servicios_view'),
]

# Agrega la URL de MEDIA files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

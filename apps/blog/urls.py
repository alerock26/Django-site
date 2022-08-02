from django.urls import path
from .views import all_posts_view

# Para agregar las url de ficheros MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', all_posts_view, name='all_posts_view' ),
]

# Agrega la URL de MEDIA files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
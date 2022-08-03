from django.urls import path
from .views import all_posts_view, posts_by_cat_id

# Para agregar las url de ficheros MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', all_posts_view, name='all_posts_view' ),
    path('categoria/<int:cat_id>', posts_by_cat_id, name='posts_by_cat_id'),
]

# Agrega la URL de MEDIA files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
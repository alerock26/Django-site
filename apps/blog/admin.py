from django.contrib import admin
from .models import Post, Categoria

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

class CategoriaAdmin(admin.ModelAdmin):
    read_only_fields = ['created', 'updated']

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def all_posts_view(request):
    all_posts = Post.objects.all()
    all_cat = Categoria.objects.all()
    return render(request, 'blog/all_posts.html', {'posts':all_posts, 'categorias':all_cat})

def unique_categories():
    all_cat = list(Categoria.objects.all())
    uniques = []
    for i in all_cat:
        if i.nombre in uniques:
            continue
        else:
            uniques.append(i.nombre)
    return uniques
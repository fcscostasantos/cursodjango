from django.shortcuts import render
from .models import Post

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados']

    list_posts = Post.objects.all()

    data = {'name': 'Curso Django3',
            'lista_tec': lista,
            'posts': list_posts}

    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})
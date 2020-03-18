from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'ray',
        'title': 'start',
        'content': 'hello web',
        'date': 'Mar 13, 2020'
    },
    {
        'author': 'amy',
        'title': 'second post',
        'content': 'hello web2',
        'date': 'Mar 13, 2020'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
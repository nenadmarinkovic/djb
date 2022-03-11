from turtle import pos, title
from django import views
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Nenad',
        'title': 'Post 1',
        'content': 'Content 1 Blog post',
        'date_posted': '11.3.2022'
    },
     {
        'author': 'Helena',
        'title': 'Post 2',
        'content': 'Content 2 Blog post',
        'date_posted': '10.3.2022'
    },
      {
        'author': 'Xxx',
        'title': 'Post 3',
        'content': 'Content 3 Blog post',
        'date_posted': '11.3.2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
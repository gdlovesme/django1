from django.shortcuts import render

from test1.models import Post


def index(request):
    posts = Post.objects.all()   #select * from Post
    return render(request, 'test1/main.html', context={'posts': posts})

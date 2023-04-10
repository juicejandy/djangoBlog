from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_posts(request):
    profiles = Profile.objects.all()
    posts = Post.objects.all()

    return render(request, 'posts/posts.html', {'profiles': profiles, 'posts': posts})


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/single_post.html', {'post': post})

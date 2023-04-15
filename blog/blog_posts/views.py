from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_page(request):
    return render(request, 'blog_posts/home_page.html')


def posts_page(request):
    posts = Post.objects.all().order_by('-pub_date')

    return render(request, 'blog_posts/posts.html', {'posts': posts})


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog_posts/single_post.html', {'post': post})
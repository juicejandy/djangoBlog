from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from blog_edit.forms import CommentForm
from django.urls import reverse


def home_page(request):
    return render(request, 'blog_posts/home_page.html')


def posts_page(request):
    posts = Post.objects.all().order_by('-pub_date')

    return render(request, 'blog_posts/posts.html', {'posts': posts})


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            print(f'text {text} \n post {post} \n request.user {request.user} \n')
            Comment.objects.create(text=text, user=request.user, post=post)
            return redirect(reverse('blog_posts:single_post', args=[pk]))
    else:
        form = CommentForm()
    return render(request, 'blog_posts/single_post.html', {'post': post, 'form': form})

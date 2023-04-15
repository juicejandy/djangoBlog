from django.shortcuts import render, redirect
from django.contrib import messages
from blog_posts.models import Post
from .forms import PostForm


def create_page(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user
            post.save()
            return redirect('blog_posts:posts_page')
    else:
        form = PostForm()
    return render(request, 'blog_edit/add_post_page.html', {'form': form})


def change_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'The post is update!')
            return redirect('blog_posts:posts_page')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_edit/create_post.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from blog_posts.models import Post, Comment
from .forms import PostForm, CommentForm


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


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('blog_posts:posts_page')


def add_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            print(f'text {text} \n post {post} \n request.user {request.user} \n')
            Comment.objects.create(text=text, user=request.user, post=post)
            return redirect('blog_posts:posts_page')
    else:
        form = CommentForm()
    return render(request, 'blog_edit/add_comment.html', {'form': form})

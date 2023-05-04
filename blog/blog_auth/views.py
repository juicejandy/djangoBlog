from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from blog_posts.models import Comment
from django.contrib import messages


def login_page(request):
    a = Comment.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Greetings {user.username}!')
            return redirect('blog_posts:posts_page')
        else:
            messages.error(request, 'Invalid login or password')
            return redirect('blog_auth:login_page')

    return render(request, 'blog_auth/login_page.html', {'a': a})


def logout_page(request):
    logout(request)
    return redirect('blog_posts:home_page')


def registration_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Greetings {user.username}!')
            return redirect('blog_posts:home_page')
        else:
            messages.error(request, 'Invalid login or password!')
            return redirect('blog_auth:registration_page')
    else:
        form = UserCreationForm()
    return render(request, 'blog_auth/registration_page.html', {'form': form})

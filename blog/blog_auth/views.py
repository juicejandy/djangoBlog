from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:home')
        else:
            error = 'Invalid login or password'
            return render(request, 'blog_auth/login_page.html', {'error': error})

    return render(request, 'blog_auth/login_page.html')


def logout_page(request):
    logout(request)
    return redirect('posts:home')


def registration_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:home')
    else:
        form = UserCreationForm()
    return render(request, 'blog_auth/registration_page.html', {'form': form})

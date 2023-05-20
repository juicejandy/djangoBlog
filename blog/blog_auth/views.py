from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from blog_posts.models import Comment
from django.contrib import messages
from django.views.generic import CreateView


# def login_page(request):
#     a = Comment.objects.all()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Greetings {user.username}!')
#             return redirect('blog_posts:posts_page')
#         else:
#             messages.error(request, 'Invalid login or password')
#             return redirect('blog_auth:login_page')
#
#     return render(request, 'blog_auth/login_page.html', {'a': a})


# def logout_page(request):
#     logout(request)
#     return redirect('blog_posts:home_page')


# def registration_page(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, f'Greetings {user.username}!')
#             return redirect('blog_posts:home_page')
#         else:
#             messages.error(request, 'Invalid login or password!')
#             return redirect('blog_auth:registration_page')
#     else:
#         form = UserCreationForm()
#     return render(request, 'blog_auth/registration_page.html', {'form': form})

class RegistrationView(CreateView):
    template_name = 'blog_auth/registration_page.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('blog_auth:login_page')

    def form_valid(self, form):
        messages.success(self.request, 'You create a new profile. Please Log In!')
        return super().form_valid(form)


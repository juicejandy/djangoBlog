from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'blog_auth'

urlpatterns = [
    path('login/', LoginView.as_view(next_page='blog_posts:posts_page', template_name='blog_auth/login_page.html'), name='login_page'),
    # path('logout/', views.logout_page, name='logout_page'),
    # path('registration/', views.registration_page, name='registration_page'),
    path('registration/', views.RegistrationView.as_view(), name='registration_page'),
    path('logout/', LogoutView.as_view(next_page='blog_posts:home_page'), name='logout_page'),
]
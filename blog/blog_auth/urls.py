from django.urls import path
from . import views

app_name = 'blog_auth'

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('registration/', views.registration_page, name='registration_page'),
]
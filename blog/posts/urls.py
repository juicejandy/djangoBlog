from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_posts, name='home'),
    path('post/<int:pk>', views.single_post, name='single_post'),
]
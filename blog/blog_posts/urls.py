from django.urls import path
from . import views

app_name = 'blog_posts'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('posts_page/', views.posts_page, name='posts_page'),
    path('post/<int:pk>', views.single_post, name='single_post'),
    path('post/<int:comment_pk>', views.single_post, name='delete_comment'),
    path('search/', views.search_page, name='search_page'),
]

from django.urls import path
from .views import *

app_name = 'blog_posts'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('posts_page/', PostsPageView.as_view(), name='posts_page'),
    path('post/<int:pk>', SinglePost.as_view(), name='single_post'),
    # path('post/<int:pk>', views.single_post, name='single_post'),
    # path('post/<int:comment_pk>', views.single_post, name='delete_comment'),
    path('search/', SearchPageView.as_view(), name='search_page'),
]

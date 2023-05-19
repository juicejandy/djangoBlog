from django.urls import path
from . import views
from .views import *

app_name = 'blog_edit'

urlpatterns = [
    # path('add_new_post/', views.create_page, name='create_post_page'),
    path('add_new_post/', CreatePostView.as_view(), name='create_post_page'),
    # path('change_post/<int:pk>/', views.change_post, name='change_post'),
    path('change_post/<int:pk>/', views.PostUpdateView.as_view(), name='change_post'),
    # path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    # path('del_comment/<int:pk>/', views.del_comment, name='del_comment'),
    path('del_comment/<int:pk>/', views.CommentDeleteView.as_view(), name='del_comment'),
    # path('edit_user/<int:pk>/', views.edit_user, name='edit_user'),
    path('edit_user/<int:pk>/', views.ProfileUpdateView.as_view(), name='edit_user'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    # path('delete_profile/', views.ProfileDeleteView.as_view(), name='delete_profile')
]

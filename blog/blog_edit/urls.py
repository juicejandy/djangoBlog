from django.urls import path
from . import views

app_name = 'blog_edit'

urlpatterns = [
    path('add_new_post/', views.create_page, name='create_post_page'),
    path('change_post/<int:pk>/', views.change_post, name='change_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
]

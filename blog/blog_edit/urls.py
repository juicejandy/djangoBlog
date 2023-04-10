from django.urls import path
from . import views

app_name = 'blog_edit'

urlpatterns = [
    path('change_post/<int:pk>', views.change_post, name='change_post'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_posts.urls')),
    path('', include('blog_auth.urls')),
    path('', include('blog_edit.urls')),
]

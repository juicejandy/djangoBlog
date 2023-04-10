from django.shortcuts import render, redirect
from .forms import *
from ..posts.models import Profile


def change_post(request, pk):
    username = Profile.objects.get(id=pk)
    if request.method == 'POST':
        form = PostEdit(request.POST, instance=username)
        if form.is_valid():
            form.save()
            return redirect('posts:home')
    else:
        form = PostEdit()
    return render(request, 'blog_edit/change.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from blog_posts.models import Post, Comment
from .forms import PostForm, CommentForm, UserForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView, UpdateView, DeleteView

User = get_user_model()


# def create_page(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.profile = request.user
#             post.save()
#             return redirect('blog_posts:posts_page')
#     else:
#         form = PostForm()
#     return render(request, 'blog_edit/add_post_page.html', {'form': form})

class CreatePostView(CreateView):
    model = Post
    template_name = 'blog_edit/add_post_page.html'
    form_class = PostForm
    success_url = reverse_lazy('blog_posts:posts_page')

    # def form_valid(self, form):
    #     form.instance.profile = self.request.user
    #     return super().form_valid(form)


# def change_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'The post is update!')
#             return redirect('blog_posts:posts_page')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog_edit/edit_post.html', {'form': form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_edit/edit_post.html'
    success_url = reverse_lazy('blog_posts:posts_page')


# def delete_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     post.delete()
#     return redirect('blog_posts:posts_page')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_posts:posts_page')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# def del_comment(request, pk):
#     print(pk)
#     comment = Comment.objects.get(pk=pk)
#     print(comment)
#     comment.delete()
#     return redirect(request.META.get('HTTP_REFERER'))


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        comment = self.get_object()
        post = comment.post
        return reverse_lazy('blog_posts:single_post', kwargs={'pk': post.pk})

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# def edit_user(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_posts:posts_page')
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'blog_edit/edit_user.html', {'form': form})

class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'blog_edit/edit_user.html'
    success_url = reverse_lazy('blog_posts:posts_page')


# def delete_profile(request):
#     if request.method == 'POST':
#         request.user.delete()
#         return redirect('blog_posts:home_page')
#     return render(request, 'blog_edit/delete_profile.html')


class ProfileDeleteView(DeleteView):
    model = User
    template_name = 'blog_edit/delete_profile.html'
    success_url = reverse_lazy('blog_posts:posts_page')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



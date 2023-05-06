from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from blog_edit.forms import CommentForm
from django.urls import reverse
from django.db.models import Q
from .models import Post
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'blog_posts/home_page.html'


class PostsPageView(ListView):
    model = Post
    template_name = 'blog_posts/posts.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-pub_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            print(f'text {text} \n post {post} \n request.user {request.user} \n')
            Comment.objects.create(text=text, user=request.user, post=post)
            return redirect(reverse('blog_posts:single_post', args=[pk]))
    else:
        form = CommentForm()
    return render(request, 'blog_posts/single_post.html', {'post': post, 'form': form, 'comments': comments})


class SearchPageView(ListView):
    template_name = 'blog_posts/search_page.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query))
        return queryset

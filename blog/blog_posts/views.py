from django.shortcuts import redirect
from .models import *
from blog_edit.forms import CommentForm
from django.urls import reverse
from django.db.models import Q
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView


class HomePageView(TemplateView):
    template_name = 'blog_posts/home_page.html'


class PostsPageView(ListView):  # отображение модели
    model = Post  # берем модель пост
    template_name = 'blog_posts/posts.html'  # указываем шаблон.(по умолчанию - другое имя)
    context_object_name = 'posts'  # указываем контекстную переменную в шаблоне(по умолчанию - другая)
    
    def get_queryset(self):  # ?(self)? Как представить наглядно?(на листке). Метод для отображения нашей модели.
        return Post.objects.order_by('-pub_date')  # Отображаем все объекты Post отсортированные по дате.(С последних)


# def single_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post=post).order_by('-pub_date')
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data.get('text')
#             print(f'text {text} \n post {post} \n request.user {request.user} \n')
#             Comment.objects.create(text=text, user=request.user, post=post)
#             return redirect(reverse('blog_posts:single_post', args=[pk]))
#     else:
#         form = CommentForm()
#     return render(request, 'blog_posts/single_post.html', {'post': post, 'form': form, 'comments': comments})


class SinglePost(DetailView):  # отображает один пост
    model = Post  # берем модель с которой будем работать(в шаблоне - object_list)
    template_name = 'blog_posts/single_post.html'  # для указания шаблона(по умолчанию другой)
    pk_url_kwarg = 'pk'  # автоматом берет данные url-параметра из URL-адреса

    def post(self, request, *args, **kwargs):  # Для отправки К. ?зачем эти аргументы откуда пост?
        pk = self.kwargs.get('pk')    # ?self.kwargs? представить как создаётся экземпляр класса
        post = self.get_object()  # ?self.get_object()?
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            Comment.objects.create(text=text, user=request.user, post=post)
        return redirect(reverse('blog_posts:single_post', args=[pk]))

    def get_context_data(self, **kwargs):  # Метод, который позволяет отображать констекст в шаблоне
        context = super().get_context_data(**kwargs)  # ?super()?, это позволяет не затереть контекст в классе
        comments = Comment.objects.filter(post=self.object).order_by('-pub_date')  # ?self.object?
        context['form'] = CommentForm()  # контекстная переменная формы 'CommentForm'
        context['comments'] = comments  # Контекстная переменная имени 'comments' что выше.
        return context  # ?разобраться с возвратами.?


class SearchPageView(ListView):  # Отображает список модели
    template_name = 'blog_posts/search_page.html'  # явно указали шаблон в котором будет отображать
    context_object_name = 'results'   # для обращения к коллекции по ключу 'results' в шаблоне

    def get_queryset(self):  # Метод. Как будет отображаться модель. ?self?
        query = self.request.GET.get('query')  #
        print(3, query)  # отдаст то, что ввели в поисковой строке
        queryset = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query))  # фильтрация по словам
        print(4, queryset)  # queryset, который будет в переменной results
        return queryset  # ?почему иногда возвращаем, а иногда нет?

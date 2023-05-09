from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView


# Главная страница
# 1-ый вариант
# def index(request):
#     # адрес шаблона
#     template = 'posts/index.html'
#     # положил тайтл в переменную для контекста
#     title = 'Это главная страница проекта Yatube'
#     # словарь контекста
#     context = {
#         # можно передать переменную
#         'title': title,
#         # можно передать текст прямо
#         'text': 'Главная страница'
#     }
#     return render(request, template_name=template, context=context)
# 2-ой вариант
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # показывать 10 записей на странцие
    paginator = Paginator(posts, 10)
    # получаем из реквеста номер запрошенной страницы
    page_number = request.GET.get('page')
    # получаем набор записей для страницы
    page_obj = paginator.get_page(page_number)
    title = 'Это главная страница проекта Yatube'
    context = {
        'page_obj': page_obj,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


# Страница блогов сгруппированных
@login_required
def group_posts(request, slug):
    # функция делает поиск по таблице group, ищет те объекты у которых
    # slug=slug
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/group_posts.html'
    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, template_name=template, context=context)


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template = 'posts/detail_post.html'
    context = {
        'post': post
    }
    return render(request, template_name=template, context=context)


class EditPost(UpdateView):
    model = Post
    template_name = 'posts/edit_post.html'
    fields = ['text', 'group']




from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # главная страница
    path('', views.index, name='index'),
    path('post/<int:pk>/edit', views.EditPost.as_view(), name='edit_post'),
    # Посты отфильтрованные по группам
    path('group/<slug:slug>', views.group_posts, name='group_posts'),
    path('post/<int:pk>', views.detail_post, name='detail_post'),
]

from django.contrib import admin
from .models import Post,Group


class PostAdmin(admin.ModelAdmin):
    # отображаем поля
    list_display = ['pk', 'text', 'pub_date', 'author', 'group']
    # поля текста
    search_fields = ['text']
    # фильтровать по такому полю
    list_filter = ['pub_date']
    # добавляет возможность сделать выбор группы прям в админке без
    # необходимости проваливаться в пост
    list_editable = ['group']
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']
    search_fields = ['slug']


# Регистрация модели в админке
# добавление класса отображения в админке PostAdmin
admin.site.register(Post, PostAdmin)

# Регистрация для группы
admin.site.register(Group, GroupAdmin)

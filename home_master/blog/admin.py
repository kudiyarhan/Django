# from django.contrib import admin
# from .models import Article, ArticleImage
#
#
# class ArticleImageInline(admin.TabularInline):
#     model = ArticleImage
#     extra = 1  # Сколько пустых полей показывать сразу
#     fields = ('image', 'caption')
#
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'created_at')
#     prepopulated_fields = {'slug': ('title',)}
#     search_fields = ('title', 'text')
#     inlines = [ArticleImageInline]  # ← Добавляем inline для картинок
#
#
# @admin.register(ArticleImage)
# class ArticleImageAdmin(admin.ModelAdmin):
#     list_display = ('article', 'caption')

from django.contrib import admin
from .models import Category, Article, ArticleImage


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1  # Сколько пустых полей показывать сразу
    fields = ('image', 'caption')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Автоматически генерирует slug из названия
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'created_at')
    list_filter = ('category', 'created_at')  # Фильтр по категории слева
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'text')
    inlines = [ArticleImageInline]


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('article', 'caption')
from django.contrib import admin
from .models import Article, ArticleImage


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1  # Сколько пустых полей показывать сразу
    fields = ('image', 'caption')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'text')
    inlines = [ArticleImageInline]  # ← Добавляем inline для картинок


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('article', 'caption')
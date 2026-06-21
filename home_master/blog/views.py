# from django.shortcuts import render
#
# def all_articles(request):
#     return render(request, 'blog/all_articles.html')
#
# def article(request):
#     return render(request, 'blog/article.html')

from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
    articles = Article.objects.all()  # Получаем все статьи из БД
    return render(request, 'blog/all_articles.html', {'articles': articles})


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)  # Ищем статью по slug
    return render(request, 'blog/article.html', {'article': article})
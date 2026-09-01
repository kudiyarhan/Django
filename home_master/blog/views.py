

from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
    articles = Article.objects.all()  # Получаем все статьи из БД
    return render(request, 'blog/all_articles.html', {'articles': articles})


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)  # Ищем статью по slug
    return render(request, 'blog/article.html', {'article': article})

# def tv_repair(request):
#     return render(request, 'blog/tv.html')
def tv_repair(request):
    # Получаем только опубликованные статьи, у которых категория имеет slug 'tv'
    articles = Article.objects.filter(category__slug='tv')

    return render(request, 'blog/tv.html', {'articles': articles})


def cofe_repair(request):
    articles = Article.objects.filter(category__slug='cofe')
    return render(request, 'blog/cofe.html', {'articles': articles})


def printer_repair(request):
    articles = Article.objects.filter(category__slug='3dprinter')
    return render(request, 'blog/3dprinter.html', {'articles': articles})


def laptop_repair(request):
    articles = Article.objects.filter(category__slug='laptop')
    return render(request, 'blog/laptop.html', {'articles': articles})
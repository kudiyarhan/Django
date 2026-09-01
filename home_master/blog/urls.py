
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    path('tv/', views.tv_repair, name='tv'),
    path('cofe/', views.cofe_repair, name='cofe'),
    path('3dprinter/', views.printer_repair, name='3dprinter'),
    path('laptop/', views.laptop_repair, name='laptop'),
    path('<slug:slug>/', views.article, name='article'),


]

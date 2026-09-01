# from django.db import models
#
#
# def article_main_image_path(instance, filename):
#     """Путь для главного изображения статьи: articles/<slug>/<filename>"""
#     return f'articles/{instance.slug}/{filename}'
#
#
# def article_gallery_image_path(instance, filename):
#     """Путь для дополнительного изображения: articles/<slug>/<filename>"""
#     return f'articles/{instance.article.slug}/{filename}'
#
#
# class Article(models.Model):
#     title = models.CharField(max_length=200, verbose_name="Заголовок")
#     text = models.TextField(verbose_name="Текст статьи")
#     slug = models.SlugField(unique=True, verbose_name="URL (slug)")
#     image = models.ImageField(
#         upload_to=article_main_image_path,  # ← первая функция
#         blank=True,
#         null=True,
#         verbose_name="Главное изображение"
#     )
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#
#     class Meta:
#         verbose_name = "Статья"
#         verbose_name_plural = "Статьи"
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return self.title
#
#
# class ArticleImage(models.Model):
#     article = models.ForeignKey(
#         Article,
#         related_name='images',
#         on_delete=models.CASCADE,
#         verbose_name="Статья"
#     )
#     image = models.ImageField(
#         upload_to=article_gallery_image_path,  # ← вторая функция
#         verbose_name="Изображение"
#     )
#     caption = models.CharField(
#         max_length=200,
#         blank=True,
#         verbose_name="Подпись к фото"
#     )
#
#     class Meta:
#         verbose_name = "Изображение статьи"
#         verbose_name_plural = "Изображения статей"
#
#     def __str__(self):
#         return f"Фото для: {self.article.title}"

from django.db import models
from django.urls import reverse


def article_main_image_path(instance, filename):
    """Путь для главного изображения статьи: articles/<slug>/<filename>"""
    return f'articles/{instance.slug}/{filename}'


def article_gallery_image_path(instance, filename):
    """Путь для дополнительного изображения: articles/<slug>/<filename>"""
    return f'articles/{instance.article.slug}/{filename}'


class Category(models.Model):
    """Модель категории статей"""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL (slug)")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст статьи")
    slug = models.SlugField(unique=True, verbose_name="URL (slug)")

    # === НОВОЕ ПОЛЕ: СВЯЗЬ С КАТЕГОРИЕЙ ===
    # null=True и blank=True добавлены, чтобы миграция прошла гладко,
    # если у вас уже есть старые статьи без категории.
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # Если категорию удалят, статья останется (категория станет пустой)
        related_name='articles',
        verbose_name="Категория",
        null=True,
        blank=True
    )
    # =======================================

    image = models.ImageField(
        upload_to=article_main_image_path,
        blank=True,
        null=True,
        verbose_name="Главное изображение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})


class ArticleImage(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Статья"
    )
    image = models.ImageField(
        upload_to=article_gallery_image_path,
        verbose_name="Изображение"
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Подпись к фото"
    )

    class Meta:
        verbose_name = "Изображение статьи"
        verbose_name_plural = "Изображения статей"

    def __str__(self):
        return f"Фото для: {self.article.title}"


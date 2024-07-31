from django.db import models
from django.shortcuts import reverse


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Food.Status.PUBLISHED)


class Food(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='URL', db_index=True, unique=True)
    content = models.TextField(null=True, blank=True, verbose_name='Рецепт')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # class Meta:
    #     verbose_name = 'Рецепт'
    #     verbose_name_plural = 'Рецепты'
    #     ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

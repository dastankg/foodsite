from django.db import models
from django.shortcuts import reverse


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
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Теги')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.slug or self.title
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')

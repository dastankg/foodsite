from django.db import models


# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Рецепт')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'Рецепт'
    #     verbose_name_plural = 'Рецепты'
    #     ordering = ['-created']

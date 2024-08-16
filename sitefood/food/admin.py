from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models.functions import Length

from .models import Category, Food, TagPost


# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'tags', 'is_published')
    list_display = ('title', 'updated', 'is_published', 'post_photo', 'cat')
    list_display_links = ('title',)
    ordering = ['updated']
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'cat')
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    readonly_fields = ['slug', 'post_photo']

    @admin.display(description='Photo', ordering='content')
    def post_photo(self, food: Food):
        if food.photo:
            return mark_safe(f'<img src="{food.photo.url}" width="50" height="50">')
        return 'Фото отсутствует'

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Food.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей 1')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Food.Status.DRAFT)
        self.message_user(request, f'Изменено {count} записей')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    ordering = ['name']
    # search_fields = ('name', )
    # prepopulated_fields = {'slug': ('name', )}

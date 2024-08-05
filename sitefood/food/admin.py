from django.contrib import admin
from django.db.models.functions import Length

from .models import Category, Food, TagPost

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    list_display = ('title', 'updated', 'is_published', 'brief_info')
    list_display_links = ('title',)
    ordering = ['updated']
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'cat')
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    readonly_fields = ['slug']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, food: Food):
        return f'Описание: {len(food.content)} символов'

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


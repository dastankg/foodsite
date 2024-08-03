from django import template
from django.db.models import Count
import food.views as views
from food.models import Category, TagPost
register = template.Library()


@register.inclusion_tag('food/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('food/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}

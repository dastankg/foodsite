from django import template

import food.views as views
from food.models import Category
register = template.Library()


@register.inclusion_tag('food/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

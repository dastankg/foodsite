from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

from .models import Food, Category, TagPost


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название')
    slug = forms.SlugField(max_length=255, label='URL', validators=[MinLengthValidator(3)])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Рецепт', required=False)
    is_published = forms.BooleanField(label='Опубликовано', required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
    tags = forms.ModelMultipleChoiceField(queryset=TagPost.objects.all(), label='Теги')
    field = forms.IntegerField(min_value=-100, max_value=20, validators=[
        MinValueValidator(-100), MaxValueValidator(20)
    ], error_messages={
        'MinValueValidator': 'Минимальное значение -100',
        'MaxValueValidator': 'Максимальное значение 20'
    })



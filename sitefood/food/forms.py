from django import forms
from .models import Food, Category, TagPost

class AddPostForm(forms.Form):

    title = forms.CharField(max_length=255, label='Название')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Рецепт', required=False)
    is_published = forms.BooleanField(label='Опубликовано', required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
    tags = forms.ModelMultipleChoiceField(queryset=TagPost.objects.all(), label='Теги')
    email = forms.EmailField(label='Email', required=False)


class CommentForm(forms.Form):
    username = forms.CharField(max_length = 100)
    email = forms.EmailField()
    agree = forms.BooleanField()
    content = forms.CharField(widget = forms.Textarea)
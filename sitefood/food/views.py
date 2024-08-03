from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Food, Category, TagPost

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Food.published.filter(is_published=True).select_related('cat')
    data = {'title': 'Food recipe', 'menu': menu, 'posts': posts, 'cat_selected': 0}
    return render(request, 'food/index.html', context=data)


def about(request):
    return render(request, 'food/about.html', context={'title': 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def post(request, post_slug):
    post = get_object_or_404(Food, slug=post_slug)
    data = {
        'title': post.title,
        'post': post,
        'menu': menu,
        'cat_selected': 1
    }
    return render(request, 'food/post.html', context=data)


def show_categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Food.published.filter(cat_id=category.pk).select_related('cat')
    data = {'title': f'Рецепты: {category.name}', 'menu': menu, 'posts': posts, 'cat_selected': category.pk}
    return render(request, 'food/index.html', context=data)


def show_tag_postlists(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Food.Status.PUBLISHED).select_related('cat')
    data = {'title': f'Рецепты по тегу: {tag.tag}', 'menu': menu, 'posts': posts, 'cat_selected': None}
    return render(request, 'food/index.html', context=data)

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Food

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]


cats_db = [
    {'name': 'Завтраки', 'id': 1},
    {'name': 'Супы', 'id': 2},
    {'name': 'Гарниры', 'id': 3},
    {'name': 'Десерты', 'id': 4}
]

def index(request):
    posts = Food.published.filter(is_published=True)
    data = {'title': 'Food recipe', 'menu': menu, 'posts': posts, 'cat_selected': 0}
    return render(request, 'food/index.html', context=data)


def about(request):
    return render(request, 'food/about.html', context={'title' : 'О сайте', 'menu': menu})


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

def show_categories(request, cat_id):
    posts = Food.objects.filter(is_published=True)
    data = {'title': 'Отображение по рубрикам', 'menu': menu, 'posts': posts, 'cat_selected': cat_id}
    return render(request, 'food/index.html', context=data)


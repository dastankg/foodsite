from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import AddPostForm, UploadFileForm
from .models import Food, Category, TagPost, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]


class FoodHome(TemplateView):
    template_name = 'food/index.html'
    posts = Food.published.filter(is_published=True).select_related('cat')
    extra_context = {'title': 'Food recipe', 'menu': menu, 'posts': posts, 'cat_selected': 0}


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     context['posts'] = self.posts
    #     context['title'] = 'Food recipe'
    #     context['cat_selected'] = 0
    #     return context

def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFiles()
    return render(request, 'food/about.html', context={'title': 'О сайте', 'menu': menu, 'form': form})


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


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'title': 'Добавление рецепта',
            'menu': menu,
            'form': form
        }

        return render(request, 'food/addpage.html', context=data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        data = {
            'title': 'Добавление рецепта',
            'menu': menu,
            'form': form
        }

        return render(request, 'food/addpage.html', context=data)

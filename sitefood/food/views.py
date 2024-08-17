from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import AddPostForm, UploadFileForm
from .models import Food, Category, TagPost, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]


class FoodHome(ListView):
    model = Food
    template_name = 'food/index.html'
    extra_context = {'title': 'Food recipe', 'menu': menu, 'cat_selected': 0}

    def get_queryset(self):
        return Food.published.select_related('cat')

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


class ShowPost(DetailView):
    model = Food
    template_name = 'food/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post'].title
        return context


    def get_object(self, queryset=None):
        return get_object_or_404(Food.published, slug=self.kwargs[self.slug_url_kwarg])


class FoodCategory(ListView):
    template_name = 'food/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Food.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория -' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context


class FoodTag(ListView):
    template_name = 'food/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Food.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег - ' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context


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

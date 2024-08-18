from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, UploadFileForm
from .models import Food, Category, TagPost, UploadFiles
from .templatetags.utils import DataMixin


class FoodHome(DataMixin, ListView):
    model = Food
    template_name = 'food/index.html'
    title_page = 'Главная страница'
    cat_selected = 0
    paginate_by = 3

    def get_queryset(self):
        return Food.published.select_related('cat')


def about(request):
    contact_list = Food.published.all()
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'food/about.html', context={'title': 'О сайте', 'page_obj': page_obj})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


class ShowPost(DataMixin,
               DetailView):
    model = Food
    template_name = 'food/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Food.published, slug=self.kwargs[self.slug_url_kwarg])


class FoodCategory(DataMixin, ListView):
    template_name = 'food/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Food.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title='Категрия' + cat.name, cat_selected=cat.id)


class FoodTag(DataMixin, ListView):
    template_name = 'food/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Food.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])

        return self.get_mixin_context(context, title='Тег' + tag.tag)


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm

    template_name = 'food/addpage.html'

    title_page = 'Добавление рецепта'


class UpdatePage(UpdateView):
    model = Food
    fields = ['title', 'content', 'photo', 'cat', 'tags', 'is_published']
    template_name = 'food/addpage.html'
    success_url = reverse_lazy('home')
    title = 'Редактирование рецепта'


class DeletePage(DeleteView):
    model = Food
    template_name = 'food/addpage.html'
    success_url = reverse_lazy('home')
    title = 'Удаление рецепта'

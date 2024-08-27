from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .forms import AddPostForm, ContactForm
from .models import Food, TagPost
from food.utils import DataMixin
from django.core.cache import cache


class FoodHome(DataMixin, ListView):
    model = Food
    template_name = 'food/index.html'
    title_page = 'Главная страница'
    cat_selected = 0
    paginate_by = 3

    def get_queryset(self):
        f_lst = cache.get('food_posts')
        if not f_lst:
            f_lst = Food.published.select_related('cat')
            cache.set('food_posts', f_lst, 60)
        return f_lst


@login_required
def about(request):
    contact_list = Food.published.all()
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'food/about.html', context={'title': 'О сайте', 'page_obj': page_obj})


class ContactFormView(LoginRequiredMixin, DataMixin, FormView):
    form_class = ContactForm
    success_url = reverse_lazy('home')
    template_name = 'food/contact.html'

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)


# @permission_required('food.view_food', raise_exception=True)
# def contact(request):
#     return HttpResponse('Обратная связь')


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


class AddPage(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView, ):
    form_class = AddPostForm
    template_name = 'food/addpage.html'
    title_page = 'Добавление рецепта'
    permission_required = ('food.add_food',)

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(PermissionRequiredMixin, UpdateView):
    model = Food
    fields = ['title', 'content', 'photo', 'cat', 'tags', 'is_published']
    template_name = 'food/addpage.html'
    success_url = reverse_lazy('home')
    title = 'Редактирование рецепта'
    permission_required = ('food.change_food',)


class DeletePage(DeleteView):
    model = Food
    template_name = 'food/addpage.html'
    success_url = reverse_lazy('home')
    title = 'Удаление рецепта'

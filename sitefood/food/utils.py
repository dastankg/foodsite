menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},]


class DataMixin:
    title_page = None
    extra_context = {}
    cat_selected = None
    paginate_by = 2

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page


        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    @staticmethod
    def get_mixin_context(context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context

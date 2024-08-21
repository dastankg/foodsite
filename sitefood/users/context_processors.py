from food.utils import menu


def get_food_context(request):
    context = {
        'menu': menu,
        'cat_selected': 0
    }
    return context

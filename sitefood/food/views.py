from django.http import HttpResponse, Http404
from django.shortcuts import render

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}]

data_db = [
    {
        'id': 1,
        'title': 'Спагетти Карбонара',
        'content': '''<h1>Спагетти Карбонара</h1>
        <p>Ингредиенты:</p>
        <ul>
            <li>Спагетти - 200 г</li>
            <li>Бекон - 100 г</li>
            <li>Яйца - 2 шт</li>
            <li>Пармезан - 50 г</li>
            <li>Чеснок - 2 зубчика</li>
            <li>Оливковое масло - 2 ст. л.</li>
            <li>Соль и перец - по вкусу</li>
        </ul>
        <p>Способ приготовления:</p>
        <p>1. Вскипятите воду и сварите спагетти до состояния "аль денте".</p>
        <p>2. Нарежьте бекон и обжарьте его на оливковом масле с добавлением чеснока.</p>
        <p>3. Взбейте яйца с тертым пармезаном, солью и перцем.</p>
        <p>4. Соедините спагетти с беконом и яйцами, тщательно перемешайте.</p>
        <p>5. Подавайте, посыпав оставшимся пармезаном и свежемолотым перцем.</p>''',
        'is_published': True
    },
    {
        'id': 2,
        'title': 'Куриное Филе в Кляре',
        'content': '''<h1>Куриное Филе в Кляре</h1>
        <p>Ингредиенты:</p>
        <ul>
            <li>Куриное филе - 400 г</li>
            <li>Яйца - 2 шт</li>
            <li>Мука - 100 г</li>
            <li>Молоко - 100 мл</li>
            <li>Соль и перец - по вкусу</li>
            <li>Растительное масло - для жарки</li>
        </ul>
        <p>Способ приготовления:</p>
        <p>1. Нарежьте куриное филе на порционные куски.</p>
        <p>2. Взбейте яйца с молоком, добавьте муку, соль и перец.</p>
        <p>3. Обмакните куски филе в кляре и обжарьте на разогретом масле до золотистой корочки.</p>
        <p>4. Подавайте с гарниром по вкусу.</p>''',
        'is_published': True
    },
    {
        'id': 3,
        'title': 'Шоколадный Торт',
        'content': '''<h1>Шоколадный Торт</h1>
        <p>Ингредиенты:</p>
        <ul>
            <li>Мука - 200 г</li>
            <li>Какао-порошок - 50 г</li>
            <li>Сахар - 150 г</li>
            <li>Молоко - 250 мл</li>
            <li>Яйца - 2 шт</li>
            <li>Масло сливочное - 100 г</li>
            <li>Разрыхлитель - 1 ч. л.</li>
            <li>Ванилин - по вкусу</li>
        </ul>
        <p>Способ приготовления:</p>
        <p>1. Смешайте сухие ингредиенты: муку, какао, разрыхлитель, ванилин.</p>
        <p>2. Взбейте яйца с сахаром, добавьте растопленное масло и молоко.</p>
        <p>3. Соедините сухие и жидкие ингредиенты, перемешайте до однородности.</p>
        <p>4. Выпекайте в разогретой до 180°C духовке 25-30 минут.</p>
        <p>5. Подавайте, украсив по вкусу.</p>''',
        'is_published': True
    }
]

cats_db = [
    {'name': 'Завтраки', 'id': 1},
    {'name': 'Супы', 'id': 2},
    {'name': 'Гарниры', 'id': 3},
    {'name': 'Десерты', 'id': 4}
]

def index(request):
    data = {'title': 'Food recipe', 'menu': menu, 'posts': data_db, 'cat_selected': 0}
    return render(request, 'food/index.html', context=data)


def about(request):
    return render(request, 'food/about.html', context={'title' : 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def post(request, post_id):
    return HttpResponse('Статья %s' % post_id)

def show_categories(request, cat_id):
    data = {'title': 'Отображение по рубрикам', 'menu': menu, 'posts': data_db, 'cat_selected': cat_id}
    return render(request, 'food/index.html', context=data)
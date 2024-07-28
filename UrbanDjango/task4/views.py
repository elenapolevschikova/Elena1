from django.shortcuts import render

# Create your views here.


def cart(request):
    content = {
        'pagename': 'Карзина',
        'first': 'Atomic Heart', 'second': 'Cyberpunk 2077',
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2'],
        'cart': 'Извините ваша корзина пуста',
        'menu': {
            'Главная': 'Главная',
            'Магазин': 'Магазин',
            'Карзина': 'Карзина'
        }
    }
    return render(request, 'second_task/third_task/fourth_task/cart.html', content)



def games(request):
    content = {
        'pagename': 'Игры',
        'first': 'Atomic Heart', 'second': 'Cyberpunk 2077',
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2'],
        'menu': {
            'Главная': 'Главная',
            'Магазин': 'Магазин',
            'Карзина': 'Карзина'
        }
    }
    return render(request, 'second_task/third_task/fourth_task/games.html', content)


def platform(request):
    content = {
        'pagename': 'Главная страница',
        'first': 'Atomic Heart', 'second': 'Cyberpunk 2077',
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2'],
        'menu': {
            'Главная': 'Главная',
            'Магазин': 'Магазин',
            'Карзина': 'Карзина'
        }
    }
    return render(request, 'second_task/third_task/fourth_task/platform.html', content)




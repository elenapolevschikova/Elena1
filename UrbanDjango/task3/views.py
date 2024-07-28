from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request, 'second_task/third_task/cart.html')



def games(request):
    return render(request, 'second_task/third_task/games.html')


def platform(request):
    return render(request, 'second_task/third_task/platform.html')

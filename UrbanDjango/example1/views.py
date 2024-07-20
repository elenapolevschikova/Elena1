# from django.views.generic import TemplateView
# https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami

from django.shortcuts import render
from django.http import HttpResponse   # Для отображения кусочка текста


# Create your views here.

# def index(request):   # Для отображения кусочка текста
#     return HttpResponse("<h4>Проверка работы</h4>")
#
#
# def about(request):   # Для отображения кусочка текста
#     return HttpResponse("<h4>Страница про нас</h4>")

def index(request):
    return render(request, 'example1/index.html')



def about(request):
    return render(request, 'example1/about.html')


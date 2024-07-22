from django.urls import path
from . import views


urlpatterns = [
    path('', views.platform, name='home'),
    path('games', views.games, name='games'),
    path('cart', views.cart, name='cart')
    ]

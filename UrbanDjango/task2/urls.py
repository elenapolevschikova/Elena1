from django.urls import path
from . import views


urlpatterns = [
    path('', views.classing),
    path('functional', views.functional)
]


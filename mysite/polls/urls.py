from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.newS, name='index'),
]
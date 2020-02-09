from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors_simple/', views.authors_simple, name='authors'),
    path('<int:question_id>/', views.detail, name='detail'),
]
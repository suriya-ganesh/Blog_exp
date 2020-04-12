from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutDetail.as_view(), name='about'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

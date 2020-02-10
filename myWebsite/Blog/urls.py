from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Blog, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors_simple/', views.authors_simple, name='authors'),
    path('<int:question_id>/', views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

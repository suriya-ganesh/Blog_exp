from django.contrib import admin
from .models import Author, BlogPost

admin.site.register(BlogPost)
admin.site.register(Author)
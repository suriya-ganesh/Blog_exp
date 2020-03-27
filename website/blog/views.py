from django.views import generic
from django.shortcuts import render
from .models import Post

class PostList(generic.ListView):
    model = Post
    context_object_name = 'my_post_list'
    queryset = Post.objects.filter(title__icontains='p')[:5]
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


from django.views import generic
from django.shortcuts import render
from .models import Post, Reading, About

class PostList(generic.ListView):
    model = Post
    context_object_name = 'my_post_list'
    queryset = Post.objects.all()
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        context['reading'] = Reading.objects.all()
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AboutDetail(generic.ListView):

    model = About
    template_name = 'blog/about.html'

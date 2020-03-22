from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    context_object_name = 'my_post_list'
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
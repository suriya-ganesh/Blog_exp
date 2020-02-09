from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Author
import logging
from django.shortcuts import render

# Create your views here.
def Blog(request):

    return render(request,"blog/index.html")


''' 
This is an example on how to send an input url's data into the
web page.
'''
def detail(request,question_id):

    return HttpResponse("%s" %question_id)


'''
returning a html response
uri = "/blog/authors/
'''


def authors(request):

    author_list = Author.objects.all()
    template = loader.get_template("blog/index.html")
    logging.error("!!!!!!1")
    context = {
        'latest_author_list' : author_list
    }
    return HttpResponse(template.render(context,request))


'''
returning a Html response, but with django.shortcuts.render
uri = "/blog/authors_simple"
'''


def authors_simple(request):

    author_list = Author.objects.all()
    context = {
        'latest_author_list' : author_list
    }
    return render(request,"blog/index.html",context=context)

def handler404(request, exception, template_name="404.html"):
    # response = render_to_response(template_name)
    # response.status_code = 404
    return render(request,template_name,status=404)
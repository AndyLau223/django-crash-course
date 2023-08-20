from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

# connect Models and Templates
#  - get data from database
#  - return data to html templates


class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'


class HomeView(generic.TemplateView):
    template_name = 'index.html'
from django.shortcuts import render
from .models import STATUS, Post
from django.views import generic

# Create your views here.

# Connect a model to a template.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

class AboutView(generic.TemplateView):       # use TemplateView because we don't need data from database.
    template_name = 'about.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')      # "-"表示顺序颠倒
    template_name = 'index.html'
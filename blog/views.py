from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


class ListBlog(ListView):
    model = Blog
    queryset = Blog.objects.all()
    paginate_by = 6
    context_object_name = 'blogs'
    template_name = 'pages/blog/blog.html'


class BlogDetail(DetailView):
    model = Blog
    queryset = Blog.objects.all()
    context_object_name = 'blog'
    template_name = 'pages/blog/blog-detail.html'

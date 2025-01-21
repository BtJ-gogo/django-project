from django.views.generic import ListView, DetailView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

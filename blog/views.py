from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_create.html"
    fields = "__all__"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("home")

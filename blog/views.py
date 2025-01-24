from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy

from .forms import CommentForm
from .models import Post, Comment


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 3


"""
class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
"""


class BlogDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class CommentGet(DetailView):
    model = Post
    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "blog_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog_detail", kwargs={"pk": self.get_object().pk})


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class BlogCreateView(AdminRequiredMixin, CreateView):
    model = Post
    template_name = "blog_create.html"
    fields = "__all__"


class BlogDeleteView(AdminRequiredMixin, DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("home")


class BlogUpdateView(AdminRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "blog_update.html"

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy

from .forms import CommentForm
from .models import Post, Category


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        request.session["previous_url"] = request.get_full_path()
        return super().get(request, *args, **kwargs)


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

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_path"] = self.request.get_full_path()
        return context
    """


class CommentGet(DetailView):
    model = Post
    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["previous_url"] = self.request.session.get("previous_url", "/")
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


"""
def CategoryBlogListView(request, category):
    category_obj = get_object_or_404(Category, name=category)
    category_posts = Post.objects.filter(category=category_obj)
    return render(
        request,
        "blog_list_category.html",
        {
            "category": category,
            "category_posts": category_posts,
        },
    )

    # def get_queryset(self):
    # return super().get_queryset()
"""


class CategoryBlogListView(ListView):
    model = Post
    template_name = "blog_list_category.html"  # 使用するテンプレート
    context_object_name = "category_posts"  # テンプレートで使用するオブジェクト名
    paginate_by = 3

    def get_queryset(self):
        # URLからカテゴリ名を取得して、そのカテゴリに属する投稿をフィルタリング
        category_name = self.kwargs.get("category")
        self.category = get_object_or_404(Category, name=category_name)
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # 追加のコンテキストデータを提供
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context

    def get(self, request, *args, **kwargs):
        request.session["previous_url"] = request.get_full_path()
        return super().get(request, *args, **kwargs)


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class BlogCreateView(AdminRequiredMixin, CreateView):
    model = Post
    template_name = "blog_create.html"
    fields = ["title", "author", "category", "body"]


class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    template_name = "category_create.html"
    fields = ["name"]


class BlogDeleteView(AdminRequiredMixin, DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url = reverse_lazy("home")


class BlogUpdateView(AdminRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "category", "body"]
    template_name = "blog_update.html"

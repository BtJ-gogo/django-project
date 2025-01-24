from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    HomePageView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
    BlogUpdateView,
    # AddCommentView,
)

urlpatterns = [
    # path("<int:pk>/comment/", AddCommentView.as_view(), name="comment_add"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("", HomePageView.as_view(), name="home"),
]

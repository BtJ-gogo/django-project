from django.urls import path
from .views import HomePageView, BlogDetailView, BlogCreateView, BlogDeleteView

urlpatterns = [
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", HomePageView.as_view(), name="home"),
]

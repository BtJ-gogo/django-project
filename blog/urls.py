from django.urls import path
from .views import HomePageView, BlogDetailView

urlpatterns = [
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", HomePageView.as_view(), name="home"),
]

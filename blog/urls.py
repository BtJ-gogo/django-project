from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import (
    HomePageView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
    BlogUpdateView,
    CategoryCreateView,
    CategoryBlogListView,
    BlogPostAPI,
)

router = DefaultRouter()
router.register(r"posts", BlogPostAPI)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "category/<str:category>/",
        CategoryBlogListView.as_view(),
        name="blog_list_category",
    ),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("addcategory/", CategoryCreateView.as_view(), name="category_create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("", HomePageView.as_view(), name="home"),
]

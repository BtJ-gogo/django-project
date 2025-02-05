from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Category, Post, Comment


# model test
class CategoryModelTest(TestCase):
    # check unique
    def test_category_name_unique(self):
        category = Category.objects.create(name="Test Category")
        with self.assertRaises(Exception):
            Category.objects.create(name="Test Category")

    # check str method
    def test_category_str_method(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")

    # check URL
    def test_get_absolute_url_method(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.get_absolute_url(), reverse("category_create"))


# check views
class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

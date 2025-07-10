from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user_profile.models import Profile
from recipe.models import Recipe


class DashboardViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = Profile.objects.create(user=self.user, name="Test User")
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            author=self.user,
            image="test.jpg",
            ingredients="Something",
            instructions="Do something",
        )

    def test_dashboard_all_recipes(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_dashboard_my_recipes(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("my_recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_dashboard_favourites(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("favourites"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dashboard")


class RecipeDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = Profile.objects.create(user=self.user, name="Test User")

        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            slug="chocolate-cake",
            author=self.user,
            image="cake.jpg",
            ingredients="Flour, Cocoa, Sugar",
            instructions="Mix and bake",
        )

    def test_recipe_detail_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            reverse("recipe_detail", args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chocolate Cake")

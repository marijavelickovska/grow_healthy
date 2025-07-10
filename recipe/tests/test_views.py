from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipe.models import Recipe


class AddRecipeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.url = reverse('add_recipe')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_get_add_recipe_page(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/add_recipe.html')

    def test_post_invalid_data_shows_errors(self):
        self.client.login(username='testuser', password='password123')
        # Missing required fields like title
        response = self.client.post(self.url, data={'ingredients': 'Only this'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There was an error in your submission")
        self.assertFalse(Recipe.objects.exists())

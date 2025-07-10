from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user_profile.models import Profile
from recipe.models import Recipe, Like, Comment, Favourite


class BaseTestSetup(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.profile = Profile.objects.create(user=self.user, name="Test User")
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            author=self.user,
            image="test.jpg",
            ingredients="Some ingredients",
            instructions="Some instructions",
        )
        self.like_url = reverse("recipe_like", args=[self.recipe.pk])
        self.unlike_url = reverse("recipe_unlike", args=[self.recipe.pk])
        self.detail_url = reverse("recipe_detail", args=[self.recipe.pk])


class DashboardViewTests(BaseTestSetup):
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

    def test_dashboard_add_recipe(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("add_recipe"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Have a great recipe?")


class RecipeDetailViewTest(BaseTestSetup):
    def test_recipe_detail_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")


class RecipeLikeViewTest(BaseTestSetup):
    def test_like_recipe_once(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            self.like_url, HTTP_REFERER=reverse("dashboard")
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(Like.objects.first().recipe, self.recipe)


class RecipeUnlikeViewTest(BaseTestSetup):
    def setUp(self):
        super().setUp()
        self.like = Like.objects.create(user=self.user, recipe=self.recipe)

    def test_unlike_recipe(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            self.unlike_url, HTTP_REFERER=reverse("dashboard")
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(
            Like.objects.filter(user=self.user, recipe=self.recipe).count(), 0
        )


class CommentEditViewTest(BaseTestSetup):
    def setUp(self):
        super().setUp()
        self.comment = Comment.objects.create(
            recipe=self.recipe, author=self.user, body="Original comment"
        )
        self.edit_url = reverse(
            "comment_edit", args=[self.recipe.pk, self.comment.pk]
        )

    def test_edit_comment_valid(self):
        self.client.login(username="testuser", password="testpass")
        self.client.post(
            self.edit_url, {"body": "Updated comment"}, follow=True
        )

        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, "Updated comment")


class CommentDeleteViewTest(BaseTestSetup):
    def setUp(self):
        super().setUp()
        self.comment = Comment.objects.create(
            recipe=self.recipe, author=self.user, body="This is a test comment"
        )
        self.delete_url = reverse(
            "comment_delete", args=[self.recipe.pk, self.comment.pk]
        )

    def test_comment_delete_by_author(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(self.delete_url, follow=True)
        self.assertRedirects(
            response,
            reverse("recipe_detail", args=[self.recipe.pk])
        )
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_comment_delete_by_other_user_fails(self):
        User.objects.create_user(username="otheruser", password="otherpass")
        self.client.login(username="otheruser", password="otherpass")
        response = self.client.post(self.delete_url, follow=True)
        self.assertRedirects(
            response, 
            reverse("recipe_detail", args=[self.recipe.pk])
        )
        self.assertTrue(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_comment_delete_with_get_method_fails(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(Comment.objects.filter(pk=self.comment.pk).exists())


class AddToFavouritesViewTest(BaseTestSetup):
    def test_add_recipe_to_favourites_successfully(self):
        self.client.login(username="testuser", password="testpass")
        fav_url = reverse("add_to_favourites", args=[self.recipe.pk])
        response = self.client.get(fav_url)

        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(
            Favourite.objects.filter(
                user=self.user, recipe=self.recipe).exists()
        )


class RemoveFromFavouritesViewTest(BaseTestSetup):
    def setUp(self):
        super().setUp()
        self.favourite = Favourite.objects.create(
            user=self.user, recipe=self.recipe
        )
        self.remove_url = reverse(
            "remove_from_favourites", args=[self.recipe.pk]
        )

    def test_remove_favourite_success(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(
            self.remove_url, HTTP_REFERER=reverse("dashboard")
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertFalse(
            Favourite.objects.filter(
                user=self.user, recipe=self.recipe).exists()
        )

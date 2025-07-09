from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from recipe.forms import RecipeForm
from recipe.models import Meal
from recipe.forms import CommentForm
from recipe.models import Comment


class TestRecipeForm(TestCase):
    """
    Unit tests for the RecipeForm to ensure it behaves correctly
    with valid and invalid data.
    """

    def setUp(self):
        """
        Set up test dependencies including a test user, a Meal instance,
        and a dummy uploaded image file.
        """
        self.user = User.objects.create_user(username="testuser", password="password")
        self.meal_type, _ = Meal.objects.get_or_create(name="Breakfast")
        self.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=b"fake image content",
            content_type="image/jpeg"
        )

    def test_recipe_form_is_valid(self):
        """
        Test that the RecipeForm is valid when all required fields are provided correctly.
        """
        form_data = {
            "title": "Test Recipe",
            "meal_type": [self.meal_type.id],
            "ingredients": "Flour, Eggs, Milk",
            "instructions": "Mix and cook",
            "excerpt": "Quick and easy",
        }
        recipe_form = RecipeForm(data=form_data, files={"image": self.image})
        self.assertTrue(
            recipe_form.is_valid(),
            msg="RecipeForm should be valid with correct data"
        )

    def test_recipe_form_is_invalid_without_title(self):
        """
        Test that the RecipeForm is invalid
        when the 'title' field is missing or empty.
        """
        form_data = {
            "title": "",
            "ingredients": "Flour, Eggs, Milk",
            "instructions": "Mix and cook",
            "excerpt": "Quick and easy",
            "meal_type": [self.meal_type.id],
        }
        recipe_form = RecipeForm(data=form_data, files={"image": self.image})
        self.assertFalse(
            recipe_form.is_valid(), 
            msg="RecipeForm should be invalid without a title"
        )

    def test_recipe_form_is_invalid_without_ingredients(self):
        """
        Test that the RecipeForm is invalid
        when the 'ingredients' field is missing or empty.
        """
        form_data = {
            "title": "Recipe Without Ingredients",
            "ingredients": "",
            "instructions": "Just cook",
            "excerpt": "Missing ingredients",
            "meal_type": [self.meal_type.id],
        }
        recipe_form = RecipeForm(data=form_data, files={"image": self.image})
        self.assertFalse(
            recipe_form.is_valid(),
            msg="RecipeForm should be invalid without ingredients"
        )


class TestCommentForm(TestCase):

    def test_comment_form_is_valid(self):
        """
        Test that the CommentForm is valid when a body is provided
        """
        form = CommentForm({'body': 'This is a test comment.'})
        self.assertTrue(
            form.is_valid(), msg="Form should be valid with body text")

    def test_comment_form_is_invalid_when_empty(self):
        """
        Test that the CommentForm is invalid when the body is empty
        """
        form = CommentForm({'body': ''})
        self.assertFalse(
            form.is_valid(), msg="Form should be invalid when body is empty")
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    """
    Model representing a meal type (e.g., breakfast, lunch, dinner).
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Recipe(models.Model):
    """
    Model for storing user-submitted cooking recipes.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes'
    )
    image = CloudinaryField('image')
    meal_type = models.ManyToManyField(Meal, related_name='type')
    ingredients = models.TextField()
    instructions = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.author}"


class Favourite(models.Model):
    """
    Model for storing recipes that a user has marked as favourite.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favourites'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favourited_by'
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
        ordering = ["-added_at"]

    def __str__(self):
        return f"{self.user.username} | {self.recipe.title}"


class Like(models.Model):
    """
    Model for storing user likes on recipes.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes'
        )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='liked_by'
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.user.username} liked {self.recipe.title}"


class Comment(models.Model):
    """
    Model for storing user comments on recipes.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body} by {self.author.username}"

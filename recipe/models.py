from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image')
    meal_type = models.ManyToManyField(Meal, related_name='type')
    ingredients = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | by {self.author}"

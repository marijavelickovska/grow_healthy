from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Meal(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
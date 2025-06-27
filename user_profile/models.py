from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    name = models.CharField(max_length=100, verbose_name="Your name")
    image = CloudinaryField('image', default='placeholder', blank=True)
    about = models.TextField(
        max_length=500, blank=True, verbose_name="Something about you"
    )

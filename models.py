from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name='profile')
    name = models.TextField()
    age = models.IntegerField()
    is_krutoi = models.BooleanField()

class Post(models.Model):
    text = models.TextField()
    likes_number = models.IntegerField()
    is_premium = models.BooleanField()
    
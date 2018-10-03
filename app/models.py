from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to ='images/')
    bio = models.TextField()
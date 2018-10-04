from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to ='images/')
    bio = models.TextField()

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls,identity):
        profile = Profile.objects.filter(name__username__icontains = identity)
        return profile

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 60)
    image_caption = models.CharField(max_length = 60)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0 )
    comments = HTMLField()

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def get_image(cls,id):
        image = Image.objects.filter(id = id)
        return image

    @classmethod
    def get_post(cls,jina):
        images = Image.objects.filter(profile__name__username__icontains = jina)
        return images

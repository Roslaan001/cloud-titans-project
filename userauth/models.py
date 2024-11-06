from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# from storages.backends.s3boto3 import S3Boto3Storage
from socialmedia.settings import POST_IMAGE_STORAGE, PROFILE_PICTURE_STORAGE

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profileimg = models.ImageField(upload_to='', storage=PROFILE_PICTURE_STORAGE, default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True, default='')
    

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', storage=POST_IMAGE_STORAGE)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Followers(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

    
    

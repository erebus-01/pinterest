from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  story = models.TextField(blank=True)
  firstName = models.CharField(max_length=50, blank=True)
  lastName = models.CharField(max_length=50, blank=True)
  website = models.CharField(max_length=20, blank=True)
  profileimg = models.ImageField(upload_to='profile_images', default='blank_profile.png')

  def __str__(self):
    return self.user.username

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default =uuid.uuid4)
  user = models.CharField(max_length=100)
  user_image = models.ImageField(null=True)
  image = models.ImageField(upload_to='post_images')
  caption = models.TextField()
  description = models.TextField(blank=True)
  link = models.CharField(max_length=50, blank=True)
  isActive = models.BooleanField(default=True)
  isHidden = models.BooleanField(default=False)
  isDelete = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=datetime.now)
  
  def __str__(self):
    return self.user


class FollowersCount(models.Model):
  follower = models.CharField(max_length=100)
  user = models.CharField(max_length=100)
  def __str__(self):
    return self.user
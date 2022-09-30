from django.db import models
from django.contrib.auth import get_user_model

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

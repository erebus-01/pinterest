from django.contrib import admin
from .models import Profile, Post, FollowersCount

class PostAdmin(admin.ModelAdmin):
  list_display = ['user', 'image', 'caption', 'description', 'link', 'isActive', 'isHidden', 'isDelete', 'created_at']
  search_fields = ['user', 'image', 'caption', 'description', 'link', 'created_at']
class FollowersCountAdmin(admin.ModelAdmin):
  search_fields = ['user', 'follower']
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['id_user', 'user', 'firstName', 'lastName', 'website']
  search_fields = ['firstName', 'lastName', 'website']

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(FollowersCount, FollowersCountAdmin)
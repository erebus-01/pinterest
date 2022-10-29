from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('settings', views.settings, name='settings'),
  path('upload', views.upload, name='upload'),
  path('follow', views.follow, name='follow'),
  path('all/<str:pk>', views.all, name='all'),
  path('hidden/<str:pk>', views.hidden, name='hidden'),
  path('delete/<str:pk>', views.delete, name='delete'),
  path('activePost/<str:pk>', views.activePost, name='activePost'),
  path('updatePost/<str:pk>', views.updatePost, name='updatePost'),
  path('deletePost/<str:pk>', views.deletePost, name='deletePost'),
  path('deleteForever/<str:pk>', views.deleteForever, name='deleteForever'),
  path('hiddenPost/<str:pk>', views.hiddenPost, name='hiddenPost'),
  path('profile/<str:pk>', views.profile, name='profile'),
  path('pin/<str:pk>', views.pin, name='pin'),
  path('my_profile/<str:pk>', views.my_profile, name='my_profile'),
  path('pinterest', views.signup, name='signup'),
  path('pinterest', views.logout, name='logout'),
]
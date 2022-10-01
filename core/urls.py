from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('settings', views.settings, name='settings'),
  path('upload', views.upload, name='upload'),
  path('profile', views.profile, name='profile'),
  path('pinterest', views.signup, name='signup'),
  path('pinterest', views.logout, name='logout'),
]
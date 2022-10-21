from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('settings', views.settings, name='settings'),
  path('upload', views.upload, name='upload'),
  path('follow', views.follow, name='follow'),
  path('all/<str:pk>', views.all, name='all'),
  path('profile/<str:pk>', views.profile, name='profile'),
  path('pin/<str:pk>', views.pin, name='pin'),
  path('my_profile/<str:pk>', views.my_profile, name='my_profile'),
  path('pinterest', views.signup, name='signup'),
  path('pinterest', views.logout, name='logout'),
]
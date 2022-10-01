from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('settings', views.settings, name='settings'),
  path('pinterest', views.signup, name='signup'),
  path('pinterest', views.logout, name='logout'),
]
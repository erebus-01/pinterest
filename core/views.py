from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
import os
import random

# Create your views here.
@login_required(login_url='signup')
def index(request):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'
  
  posts = list(Post.objects.all().filter(isActive=True))
  posts = random.sample(posts, len(posts))
  print(Post.objects.all().filter(isActive=True))
  return render(request, 'home.html', {'user_profile': user_profile, 'posts': posts})

@login_required(login_url='signup')
def settings(request):
  # user_profile = Profile.objects.filter(user=request.user)
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'

  if request.method == 'POST':
    if request.FILES.get('image') == None:
      image = user_profile.profileimg
      firstName = request.POST['fName_profile']
      lastName = request.POST['lName_profile']
      story = request.POST['story_profile']
      website = request.POST['website_profile']

      user_profile.profileimg = image
      user_profile.firstName = firstName
      user_profile.lastName = lastName
      user_profile.story = story
      user_profile.website = website
      user_profile.save()

    if request.FILES.get('image') != None:
      if(len(user_profile.profileimg) > 0 and str(user_profile.profileimg) != 'blank_profile.png'):
        os.remove(user_profile.profileimg.path)
      image = request.FILES.get('image')
      firstName = request.POST['fName_profile']
      lastName = request.POST['lName_profile']
      story = request.POST['story_profile']
      website = request.POST['website_profile']

      user_profile.profileimg = image
      user_profile.firstName = firstName
      user_profile.lastName = lastName
      user_profile.story = story
      user_profile.website = website
      user_profile.save()

    return redirect('settings')
  
  return render(request, 'settings.html', {'user_profile': user_profile})

@login_required(login_url='signup')
def profile(request):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'
  print(user_profile)
  return render(request, 'profile.html', {'user_profile': user_profile})

@login_required(login_url='signup')
def upload(request):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'
  print(user_profile.profileimg)
  if request.method == 'POST':
    user = request.user.username
    user_image = user_profile.profileimg
    image = request.FILES.get('upload_image')
    caption = request.POST['pin_caption']
    description = request.POST['pin_description']
    link = request.POST['pin_link']

    new_post = Post.objects.create(user=user, user_image=user_image, image=image, caption=caption, description=description, link=link)
    new_post.save()

    return redirect('/upload')
  return render(request, 'upload.html', {'user_profile': user_profile})



def signup(request):

  if 'signupBottom' in request.POST:
    email_bottom = request.POST['email_bottom']
    username_bottom = request.POST['username_bottom']
    pass_bottom = request.POST['pass_bottom']
    print(email_bottom)

    if len(pass_bottom) < 6 or len(pass_bottom) > 30:
      messages.info(request, "Password must be at least 6 characters longer than the password.")
      return redirect('signup')
    else:
      if User.objects.filter(email=email_bottom).exists():
        messages.info(request, "Email already exists!!!")
        return redirect('signup')
      elif User.objects.filter(username=username_bottom).exists():
        messages.info(request, "Username already exists!!!")
        return redirect('signup')
      else:
        user = User.objects.create_user(email=email_bottom, username=username_bottom, password=pass_bottom)
        user.save()

        user_login = User.objects.get(username=username_bottom)
        auth.login(request, user_login)

        user_model = User.objects.get(username=username_bottom)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        messages.success(request, "Account ready to login!!!")
        return redirect('settings')


  if 'signup_modal' in request.POST:
    email_signup = request.POST['email_signup']
    user_signup = request.POST['user_signup']
    pass_signup = request.POST['pass_signup']
    print(email_signup)

    if len(pass_signup) < 6 or len(pass_signup) > 30:
      messages.info(request, "Password must be at least 6 characters longer than the password.")
      return redirect('signup')
    else:
      if User.objects.filter(email=email_signup).exists():
        messages.info(request, "Email already exists!!!")
        return redirect('signup')
      elif User.objects.filter(username=user_signup).exists():
        messages.info(request, "Username already exists!!!")
        return redirect('signup')
      else:
        user = User.objects.create_user(email=email_signup, username=user_signup, password=pass_signup)
        user.save()
        
        user_login = User.objects.get(username=user_signup)
        auth.login(request, user_login)

        user_model = User.objects.get(username=user_signup)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        messages.success(request, "Account ready to login!!!")
        return redirect('signup')

  if 'loginModal' in request.POST:    
    emailModal = request.POST['emailModal']
    passModal = request.POST['passModal']
    user = auth.authenticate(username=emailModal, password=passModal)
    print(user)

    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, "Login failed !!!")
      return redirect('signup')

  else:
    return render(request, 'pinterest.html')


@login_required(login_url='signup')
def logout(request):
  auth.logout(request)
  return render(request, 'signup.html')

  
# @login_required(login_url='signup')
# def upload(request):
#   if Profile.objects.filter(user = request.user).exists():
#     user_profile = Profile.objects.get(user = request.user)
#   else:
#     user_profile = 'None profile'
#   return render(request, 'upload.html', {'user_profile': user_profile})
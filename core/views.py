from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required(login_url='signup')
def index(request):
  return render(request, 'home.html')


@login_required(login_url='signup')
def settings(request):
  return render(request, 'settings.html')

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

        user_model = User.objects.get(username=username_bottom)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        messages.success(request, "Account ready to login!!!")
        return redirect('signup')


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
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, FollowersCount
from .forms import PostForm
import os
import random
from random import randint

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
def my_profile(request, pk):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'
  
  user_following = len(FollowersCount.objects.filter(follower=pk))

  countActive = 0;
  countHidden = 0;
  countDelete = 0;

  if Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).count() > 0:
    countActive = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).count()

  if Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False).count() > 0:
    countHidden =Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False).count()

  if Post.objects.filter(user=pk, isActive=False, isDelete=True).count() > 0:
    countDelete = Post.objects.filter(user=pk, isActive=False, isDelete=True).count()

  post_last_1 = ''
  post_last_2 = ''
  post_last_3 = ''
  post_last_4 = ''
  post_last_5 = ''

  if countActive >= 1:
    post_last_1 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).last()
  if countActive >= 2:
    post_last_1 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).last()
    post_last_2 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]
  if countActive >= 3:
    post_last_1 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).last()
    post_last_2 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]
    post_last_3 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).first()
  if countActive >= 4:
    post_last_1 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).last()
    post_last_2 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]
    post_last_3 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).first()
    post_last_4 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]
  if countActive >= 5:
    post_last_1 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).last()
    post_last_2 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]
    post_last_3 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False).first()
    post_last_4 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]
    post_last_5 = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)[randint(0, countActive - 1)]

  hidden_last_1 = ''
  hidden_last_2 = ''
  hidden_last_3 = ''
  if countHidden >= 1:
    hidden_last_1 = Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False).last()
  if countHidden >= 2:
    hidden_last_1 = Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False).last()
    hidden_last_2 = Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False)[randint(0, countHidden - 1)]
  if countHidden > 3:
    hidden_last_1 = Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False).last()
    hidden_last_2 = Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False)[randint(0, countHidden - 1)]
    hidden_last_3 = Post.objects.filter(user=pk, isActive=False, isHidden=True, isDelete=False)[randint(0, countHidden - 1)]

  delete_last_1 = ''
  delete_last_2 = ''
  delete_last_3 = ''
  if countDelete >= 1:
    delete_last_1 = Post.objects.filter(user=pk, isActive=False, isHidden=False, isDelete=True).last()
  if countDelete >= 2:
    delete_last_1 = Post.objects.filter(user=pk, isActive=False, isHidden=False, isDelete=True).last()
    delete_last_2 = Post.objects.filter(user=pk, isActive=False, isHidden=False, isDelete=True)[randint(0, countDelete - 1)]
  if countDelete > 3:
    delete_last_1 = Post.objects.filter(user=pk, isActive=False, isHidden=False, isDelete=True).last()
    delete_last_2 = Post.objects.filter(user=pk, isActive=False, isHidden=False, isDelete=True)[randint(0, countDelete - 1)]
    delete_last_3 = Post.objects.filter(user=pk, isActive=False, isHidden=False, isDelete=True)[randint(0, countDelete - 1)]

  content = {
    'user_profile': user_profile,
    'countActive': countActive,
    'countHidden': countHidden,
    'countDelete': countDelete,
    'post_last_1': post_last_1,
    'post_last_2': post_last_2,
    'post_last_3': post_last_3,
    'post_last_4': post_last_4,
    'post_last_5': post_last_5,
    'hidden_last_1': hidden_last_1,
    'hidden_last_2': hidden_last_2,
    'hidden_last_3': hidden_last_3,
    'delete_last_1': delete_last_1,
    'delete_last_2': delete_last_2,
    'delete_last_3': delete_last_3,
    'user_following': user_following,
  }

  return render(request, 'profile.html', content)

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

@login_required(login_url='signup')
def profile(request, pk):
  user_object = User.objects.get(username__iexact=pk)
  user_profile = Profile.objects.get(user = user_object)
  user_post = Post.objects.filter(user=pk, isActive=True, isHidden=False, isDelete=False)
  user_post_length = len(user_post)

  follower = request.user.username
  user = pk

  print('userUpper'+user)

  if FollowersCount.objects.filter(follower=follower, user=user).first():
    button_text = "Ng?????i ??ang theo d??i"
  else:
    button_text = "Theo d??i"

  user_followers = len(FollowersCount.objects.filter(user=pk))
  user_following = len(FollowersCount.objects.filter(follower=pk))

  context = {
    'user_profile': user_profile,
    'user_object': user_object,
    'user_post': user_post,
    'user_post_length': user_post_length,
    'button_text': button_text,
    'user_followers': user_followers,
    'user_following': user_following,
  }

  return render(request, 'your_profile.html', context)

@login_required(login_url='signup')
def all(request, pk):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'

  userPost = Post.objects.all().filter(user=pk, isActive=True, isHidden=False, isDelete=False)

  context = {
    'userPost': userPost,
    'user_profile': user_profile
  }

  return render(request, 'ghim.html', context)

@login_required(login_url='signup')
def hidden(request, pk):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'

  userPost = Post.objects.all().filter(user=pk, isActive=False, isHidden=True, isDelete=False)

  context = {
    'userPost': userPost,
    'user_profile': user_profile
  }

  return render(request, 'hidden.html', context)

@login_required(login_url='signup')
def delete(request, pk):
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'

  userPost = Post.objects.all().filter(user=pk, isActive=False, isHidden=False, isDelete=True)

  context = {
    'userPost': userPost,
    'user_profile': user_profile
  }

  return render(request, 'delete.html', context)

@login_required(login_url='signup')
def updatePost(request, pk):  
  updatePost = Post.objects.get(id=pk)
  user = request.POST['user_input']
  if 'updatePost' in request.POST:
    caption = request.POST['edit_title']
    description = request.POST['edit_description']
    link = request.POST['edit_link']
    print("caption: %s, description: %s, link: %s" % (caption, description, link))
    
    updatePost.caption = caption
    updatePost.description = description
    updatePost.link = link
    updatePost.save()
    return redirect('/all/'+user)
  else:
    return redirect('/all/'+user)

@login_required(login_url='signup')
def deletePost(request, pk):
  updatePost = Post.objects.get(id=pk)
  user = request.POST['user_input']
  if 'deletePost' in request.POST:
    if updatePost.isDelete is False:
      updatePost.isActive = False
      updatePost.isHidden = False
      updatePost.isDelete = True
      updatePost.save()
      return redirect('/all/'+user)

  return redirect('/all/'+user)

@login_required(login_url='signup')
def deleteForever(request, pk):
  updatePost = Post.objects.get(id=pk)
  user = request.POST['user_input']
  if 'deleteForever' in request.POST:
    updatePost.delete()
    return redirect('/all/'+user)
  return redirect('/all/'+user)

@login_required(login_url='signup')
def hiddenPost(request, pk):
  updatePost = Post.objects.get(id=pk)
  user = request.POST['user_input']
  if 'hiddenPost' in request.POST:
    if updatePost.isHidden is False:
      updatePost.isActive = False
      updatePost.isHidden = True
      updatePost.isDelete = False
      updatePost.save()
      return redirect('/all/'+user)

  return redirect('/all/'+user)

@login_required(login_url='signup')
def activePost(request, pk):
  updatePost = Post.objects.get(id=pk)
  user = request.POST['user_input']
  if 'activePost' in request.POST:
    if updatePost.isActive is False:
      updatePost.isActive = True
      updatePost.isHidden = False
      updatePost.isDelete = False
      updatePost.save()
      return redirect('/all/'+user)

  return redirect('/all/'+user)

@login_required(login_url='signup')
def pin(request, pk):
  post = get_object_or_404(Post, id=pk)
  if Profile.objects.filter(user = request.user).exists():
    user_profile = Profile.objects.get(user = request.user)
  else:
    user_profile = 'None profile'
  user_followers = len(FollowersCount.objects.filter(user=post.user))

  postActive = Post.objects.filter(user = post.user, isActive = True, isHidden = False, isDelete=False)

  context = {
    'post': post,
    'postActive': postActive,
    'user_followers': user_followers,
    'user_profile': user_profile,
  }

  return render(request, 'pin.html', context);

@login_required(login_url='signup')
def follow(request):
  if request.method == 'POST':
    follower = request.POST['follower']
    user = request.POST['user']

    if FollowersCount.objects.filter(follower=follower,user=user).first():
      delete_follower = FollowersCount.objects.get(follower=follower,user=user)
      delete_follower.delete()
      return redirect('/profile/'+user)
    else:
      new_follower = FollowersCount.objects.create(follower=follower, user=user)
      new_follower.save()
      return redirect('/profile/'+user)

  else:
    return redirect('/')

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
      elif User.objects.filter(username=username_bottom.capitalize()).exists():
        messages.info(request, "Username already exists!!!")
        return redirect('signup')
      else:
        user = User.objects.create_user(email=email_bottom, username=username_bottom.capitalize(), password=pass_bottom)
        user.save()

        user_login = User.objects.get(username=username_bottom.capitalize())
        auth.login(request, user_login)

        user_model = User.objects.get(username=username_bottom.capitalize())
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
      elif User.objects.filter(username=user_signup.capitalize()).exists():
        messages.info(request, "Username already exists!!!")
        return redirect('signup')
      else:
        user = User.objects.create_user(email=email_signup, username=user_signup.capitalize(), password=pass_signup)
        user.save()
        
        user_login = User.objects.get(username=user_signup.capitalize())
        auth.login(request, user_login)

        user_model = User.objects.get(username=user_signup.capitalize())
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

from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm

# from users.models import User

def profile(request):
  if request.method == 'POST':
    form =  UserProfileForm(data=request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('users:profile'))
  else: 
    form = UserProfileForm(instance=request.user)
  context = {'form': form} 
  return render(request, 'user/profile.html', context)

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('index'))
  else:
    form = UserRegistrationForm()
  context = { 'form': form }
  return render(request, 'auth/register.html', context)

def login(request):
  if request.method == 'POST':
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))
 
  else:
    form = UserLoginForm()
  context = {'form': UserLoginForm()}
  return render(request, 'auth/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
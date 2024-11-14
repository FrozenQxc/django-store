from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from products.models import Basket, Product
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm


# from users.models import User
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else: 
        form = UserProfileForm(instance=request.user)
        
    context = {
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    } 
    return render(request, 'user/profile.html', context)

@login_required
def basket_add(request, product_id):
  product = Product.objects.get(id=product_id)
  baskets = Basket.objects.filter(user=request.user, product=product)
  
  if not baskets.exists():
    Basket.objects.create(user=request.user, product=product, quantity=1)
  else:
    baskets = baskets.first()
    baskets.quantity += 1
    baskets.save() 
  
  return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):  
    basket = Basket.objects.get(id=basket_id)  
    basket.delete()  
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Вы успешно зарегистрировались')
      return HttpResponseRedirect(reverse('users:login'))
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
  context = {'form': form}
  return render(request, 'auth/login.html', context)


def logout(request):
  auth.logout(request)
  return HttpResponseRedirect(reverse('index'))
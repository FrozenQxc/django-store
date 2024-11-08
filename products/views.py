from django.shortcuts import render

from products.models import Product, ProductCategory, Slider

#! функции = контроллеры = вьюхи

def index(request):
  return render(request, 'products/index.html')

def products(request): 
  context = {
    'products': Product.objects.all(),
    'categories': ProductCategory.objects.all(),
    'sliders': Slider.objects.all()
  }

  return render(request, 'products/products.html', context )

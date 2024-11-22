from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import Product, ProductCategory, Slider

#! функции = контроллеры = вьюхи

def index(request):
  return render(request, 'products/index.html')

def products(request, category_id=None, page_number=1):
  products = Product.objects.filter(category_id = category_id) if category_id else Product.objects.all()

  per_page = 3
  paginator = Paginator(products, per_page)
  products_paginator = paginator.page(page_number)
   
    
  context = {
    'categories': ProductCategory.objects.all(),
    'sliders': Slider.objects.all(),
    'products': products_paginator
  }    
    
  return render(request, 'products/products.html', context )

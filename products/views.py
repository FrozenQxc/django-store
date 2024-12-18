from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import Product, ProductCategory, Slider
from blog.models import Blog

#! функции = контроллеры = вьюхи

def index(request):
    latest_news = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'latest_news': latest_news
    }
    return render(request, 'products/index.html', context)

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

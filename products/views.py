from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import Product, ProductCategory, Slider
from blog.models import Blog

from django.shortcuts import render, redirect
from .models import Basket
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Order

#! функции = контроллеры = вьюхи

# views.py
from .models import Basket, Order, OrderItem

@login_required
def order_view(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = baskets.total_sum()
    
    if request.method == 'POST':
        address = request.POST.get('address')
        
        # Создаём заказ
        order = Order.objects.create(user=request.user, address=address)

        # Добавляем товары в заказ
        for basket in baskets:
            OrderItem.objects.create(
                order=order,
                product=basket.product,
                quantity=basket.quantity,
                price=basket.product.price,
            )
        
        # Очищаем корзину
        baskets.delete()

        return redirect('products:order_success', order_id=order.id)

    return render(request, 'products/order.html', {'baskets': baskets, 'total_sum': total_sum})

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'products/order_success.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    
    # Считаем сумму для каждого заказа
    for order in orders:
        order.total_price = sum(item.price * item.quantity for item in order.items.all())
    
    return render(request, 'products/order_list.html', {'orders': orders})


@login_required
def confirm_order(request):
    if request.method == 'POST':
        # Обработка подтверждения заказа
        address = request.POST.get('address')
        # Здесь вы можете передать информацию менеджеру, например, через email
        # Очистите корзину после успешного оформления заказа
        Basket.objects.filter(user=request.user).delete()
        return redirect('products:success_page')  # перенаправление на страницу успеха
    return redirect('products:order')

def index(request):
    latest_news = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'latest_news': latest_news
    }
    return render(request, 'products/index.html', context)
  
def about(request):
    return render(request, 'products/about.html' )  

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

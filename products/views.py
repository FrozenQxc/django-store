from django.shortcuts import render

#! функции = контроллеры = вьюхи

def index(request):
  context = {
    'title': 'Test Title',
    'username': 'valera'
  }
  return render(request, 'products/index.html')


def products(request): 
  return render(request, 'products/products.html')
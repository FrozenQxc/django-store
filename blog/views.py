from django.shortcuts import render

from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import datetime

from .forms import BlogForm, CommentForm, Feedback
from .models import Blog, Category, Comment



@login_required    
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.image = request.FILES['image'] # имя поля для загрузки изображения
            new_blog.save()
            return redirect('account')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


@login_required    
def change_blog(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            if 'image' in request.FILES:
                blog.image = request.FILES['image']
            form.save()
            return redirect('account')
        else:
            return render(request, 'blog/change_blog.html', {'blog': blog, 'form': form, 'error': 'Ошибка'})
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog/change_blog.html', {'blog': blog, 'form': form})


@login_required    
def delete_blog(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('account')

def detail(request, blog_id):
    # Получаем блог по ID
    blog = get_object_or_404(Blog, pk=blog_id)
    # Получаем все комментарии для этого блога
    comments = Comment.objects.filter(post=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = blog
            comment_f.save()
            return redirect('blog:detail', blog_id=blog_id)
    else:
        form = CommentForm()

    return render(request, 'detail.html', {'blog': blog, 'form': form, 'comments': comments})

def blog(request):
    categories = Category.objects.all() 
    blogs = Blog.objects.all() 
    if request.method == 'POST': 
        category_id = request.POST.get('category_id') 
        category = get_object_or_404(Category, id=category_id) 
        blogs = Blog.objects.filter(categories=category) 
    return render(request, 'index.html', {'categories': categories, 'blogs':blogs})


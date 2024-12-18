from django.conf import settings
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  # Добавь описание
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Добавь изображение
    categories = models.CharField(max_length=255, null=True, blank=True)  # Добавь категории
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
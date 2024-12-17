from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Админ'),
        ('manager', 'Менеджер'),
        ('user', 'Пользователь'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    def __str__(self):
        return self.username


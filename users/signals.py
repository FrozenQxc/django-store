from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def set_role_for_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser:  # если пользователь только что создан и это суперпользователь
        instance.role = 'admin'
        instance.save()

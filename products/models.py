from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class ProductCategory(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField(null=True, blank=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  quantity = models.PositiveIntegerField(default=0)
  image = models.ImageField(upload_to='products_images')
  
  category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE) # Привязка к категории 

  def __str__(self):
    return f'Продукт: {self.name} | Категория: {self.category}'
  
class Slider(models.Model):
    name = models.CharField(max_length=128)  
    image = models.ImageField(upload_to='slide_images')

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Slider)
def delete_slider_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)  # False чтобы не сохранять модель
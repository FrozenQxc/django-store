from django.contrib import admin

from products.models import Product, ProductCategory, Slider

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Slider)
from django.contrib import admin

from products.models import Product, ProductCategory, Slider, Basket

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Slider)
admin.site.register(Basket)
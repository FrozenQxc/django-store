from django.contrib import admin
from products.models import Basket, Product, ProductCategory, Slider, Order, OrderItem

admin.site.register(ProductCategory)
admin.site.register(Slider)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity', 'price')
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'address')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email', 'address')
    ordering = ('-created_at',)
    inlines = [
        OrderItemInline,  # Используем OrderItemInline для отображения товаров в заказе
    ]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order',)
    search_fields = ('product__name',)

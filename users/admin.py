from django.contrib import admin
from products.admin import BasketAdmin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email', 'date_joined')  
    list_filter = ('role',)  
    search_fields = ('username', 'email') 
    inlines = [BasketAdmin]  
  
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'role', 'image')  
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

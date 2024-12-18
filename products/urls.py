from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import (
    about,
    confirm_order,
    order_list,
    order_success,
    order_view,
    products,
)
from users.views import basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('order/', order_view, name='order'),
    path('orders/', order_list, name='order_list'),  
    path('order/confirm/', confirm_order, name='confirm_order'),
    path('order/success/<int:order_id>/', order_success, name='order_success'),
    
    path('', products, name='index'),
    path('about/', about , name='about'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

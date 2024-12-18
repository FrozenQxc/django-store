# основной файл urls.py проекта
from django.urls import path, include
from products.views import products
from users.views import basket_add, basket_remove
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='index'),
    
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('blog/', include('blog.urls', namespace='blog')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

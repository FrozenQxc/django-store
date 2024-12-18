
from django.urls import path
from blog.views import blog, detail

app_name = 'blog' 

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('<int:blog_id>/', detail, name='detail'),
]

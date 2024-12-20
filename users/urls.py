from django.urls import path

from users.views import login, logout, profile, register, user_list

app_name = 'users'

urlpatterns = [
	path('register/', register, name='register'),
	path('login/', login, name='login'),
	path('profile/', profile, name='profile'),
	path('logout/', logout, name='logout'),
	path('user_list/', user_list, name='user_list')
]
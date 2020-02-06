from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('service/', user_view.service, name='service'),
    path('profile/', user_view.profile, name='profile'),
    path('message/', user_view.messagesPage, name='messagesPage'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('clients/<str:username>/', user_view.clients),
    path('clientsm/<str:user>/', user_view.clientsm),
    path('', include('blog.urls')),
]

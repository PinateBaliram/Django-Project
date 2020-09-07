from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', views.UserRegister,name='user_register' ),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='user_logout'),


]

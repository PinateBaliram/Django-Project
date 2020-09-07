from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='to_do_home'),
    path('task/update/<int:pk>/', views.update, name='task_update'),
    path('task/delete/<int:pk>/', views.delete, name='task_delete'),

]

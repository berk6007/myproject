from django.urls import path
from . import views 

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.task_create, name='task-add'),
    path('edit/<int:pk>/', views.task_update, name='task-edit'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
    

   ]


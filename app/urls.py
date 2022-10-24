from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signUp, name='signUp'),
    path('login/', views.logIn, name='logIn'),
    path('tasks/', views.getTasks, name='getTasks'),
    path('addtask/', views.addTask, name='addTask'),
    path('deletetask/', views.deleteTask, name='deleteTask'),
    path('completed/', views.completed, name='completed'),
]
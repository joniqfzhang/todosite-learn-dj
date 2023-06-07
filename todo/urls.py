"""
URL configuration for todosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import detail

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_todo, name='create-todo'),
    path('todo/<id>/', views.todo_detail, name='todo'),
    path('todo-delete/<id>/', views.todo_delete, name='todo-delete'),
    path('edit-todo/<id>/', views.todo_edit, name='todo-edit'),  ### watch for path and name
]

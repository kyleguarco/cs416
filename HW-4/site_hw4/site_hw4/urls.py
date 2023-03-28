"""site_hw4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import todo.views as todo_views

app_name = 'todo'
urlpatterns = [
    path('', todo_views.make_views, name='todo_index'),
    path('complete/<int:id>', todo_views.complete_task, name='todo_complete'),
    path('update/<int:id>', todo_views.update_task, name='todo_update'),
    path('delete/<int:id>', todo_views.delete_view, name='todo_delete_view'),
    path('delete/<int:id>/confirm', todo_views.delete_task, name='todo_delete'),
    path('admin/', admin.site.urls),
]

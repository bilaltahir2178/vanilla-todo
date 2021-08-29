"""vanilla URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todo/', include('todo.urls'), name='todo'),
    path('admin/', admin.site.urls, name='admin'),
]

"""vanilla URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('todo/', include('todo.urls'), name='todo'),
    path('admin/', admin.site.urls, name='admin'),
]

"""todo URL Configuration
"""
from django.urls import path

from todo.api.views import (apiOverview, createTask, deleteTask, taskDetails,
                            tasksList, updateTask)

urlpatterns = [
    path('', apiOverview, name='overview'),
    path('api/list/', tasksList, name='list'),
    path('api/details/<str:pk>', taskDetails, name='details'),
    path('api/create/', createTask, name='create'),
    path('api/update/<str:pk>', updateTask, name='update'),
    path('api/delete/', deleteTask, name='delete'),
]

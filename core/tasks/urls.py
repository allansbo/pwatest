from django.urls import path

from .views import task_list, task_create, task_delete, TaskUpdate

app_name = 'tasks'

urlpatterns = [
    path('read_all/', task_list, name='list'),
    path('create/', task_create, name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', task_delete, name='delete'),
]

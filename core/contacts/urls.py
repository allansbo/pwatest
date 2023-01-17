from django.urls import path

from .views import contact_list, contact_create, contact_delete, contact_update

app_name = 'contacts'

urlpatterns = [
    path('read_all/', contact_list, name='list'),
    path('create/', contact_create, name='create'),
    path('delete/<int:pk>/', contact_delete, name='delete'),
    path('update/<int:pk>/', contact_update, name='update')
]

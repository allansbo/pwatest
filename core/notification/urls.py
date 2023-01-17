from django.urls import path

from .views import home, geolocation

app_name = 'notifications'

urlpatterns = [
    path('', home, name='home'),
    path('geolocation/', geolocation, name='geolocation')
]

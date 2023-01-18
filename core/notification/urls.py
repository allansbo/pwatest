from django.urls import path

from .views import home, geolocation, camera, notification

app_name = 'notifications'

urlpatterns = [
    path('', home, name='home'),
    path('geolocation/', geolocation, name='geolocation'),
    path('camera/', camera, name='camera'),
    path('notification/', notification, name='notification'),
]

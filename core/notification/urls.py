from django.urls import path

from .views import home, geolocation, camera, notification, inputs, service_worker

app_name = 'notifications'

urlpatterns = [
    path('', home, name='home'),
    path('OneSignalSDKWorker.js', service_worker),
    path('geolocation/', geolocation, name='geolocation'),
    path('camera/', camera, name='camera'),
    path('notification/', notification, name='notification'),
    path('inputs/', inputs, name='inputs'),
]

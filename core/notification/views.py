from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def geolocation(request):
    return render(request, 'geolocation.html')


@login_required
def camera(request):
    return render(request, 'camera.html')


@login_required
def notification(request):
    return render(request, 'notification.html')

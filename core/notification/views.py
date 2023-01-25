import os.path

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from webpush import send_user_notification

from core import settings


@login_required
def home(request):
    return render(request, 'index.html')


def service_worker(request):
    sw_path = os.path.join(settings.BASE_DIR, 'core/notification/static/js/OneSignalSDKWorker.js')
    return HttpResponse(open(sw_path).read(), content_type='application/javascript')


@login_required
def geolocation(request):
    return render(request, 'geolocation.html')


@login_required
def camera(request):
    return render(request, 'camera.html')


@login_required
def notification(request):

    if request.method == 'POST':
        head = request.POST.get('head')
        body = request.POST.get('body')

        payload = {"head": head, "body": body}

        send_user_notification(user=request.user, payload=payload, ttl=1000)

    return render(request, 'notification.html')


@login_required
def inputs(request):
    return render(request, 'inputs.html')

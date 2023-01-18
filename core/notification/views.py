from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from webpush import send_user_notification


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

    if request.method == 'POST':
        head = request.POST.get('head')
        body = request.POST.get('body')

        payload = {"head": head, "body": body}

        send_user_notification(user=request.user, payload=payload, ttl=1000)

    return render(request, 'notification.html')

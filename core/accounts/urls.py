from django.urls import path

from core.accounts.views import SignUp

app_name = 'accounts'

urlpatterns = [
    path('register/', SignUp.as_view(), name='signup')
]

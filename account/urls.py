from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.urls import path
from account.views import login_redirect


urlpatterns = [
    path('login/', login_redirect, name='login_auth'),

]

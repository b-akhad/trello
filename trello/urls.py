from django.urls import path
from trello.views import (registration, home, profile)

urlpatterns = [
    path("register/", registration, name='register'),
    path("", home, name='home'),
    path("profile/<int:pk>", profile, name='profile'),

]
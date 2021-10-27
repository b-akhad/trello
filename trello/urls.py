from django.urls import path
from trello.views import (registration, home)

urlpatterns = [
    path("register/", registration, name='register'),
    path("", home, name='home'),

]
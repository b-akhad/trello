from django.urls import path
from trello.views import (registration, home, profile, dashboard, create_organization)

urlpatterns = [
    path("register/", registration, name='register'),
    path("", home, name='home'),
    path("profile/<int:pk>", profile, name='profile'),
    path("dashboard/<int:pk>", dashboard, name='dashboard'),
    path("dashboard/create/organization",create_organization , name='create_org'),


]
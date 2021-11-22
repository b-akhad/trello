# Create your views here.
import time
import requests
import uuid
from os.path import join
from django.contrib.auth.models import User
from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth import login
from django.contrib import messages
from django.db import IntegrityError

from django.shortcuts import render, redirect

from Trello import settings
from account.forms import UserCreation
from trello.models import Picture, Org, Project

# Create your views here.


def home(request):
    return render(request, 'home.html')


def dashboard(request, pk):
    dashboard_ = Org.objects.get(pk=pk)
    projects = Project.objects.filter(org_id=dashboard_)

    if request.method == 'POST':
        project = Project()
        project.name = request.POST.get('project')
        project.org = dashboard_
        project.save()
    content = {"dashboard":dashboard_, 'projects':projects}
    return render(request, "dashboard.html",content)


def create_organization(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == "POST":
        try:
            org = Org()
            org.name = request.POST.get("org_name")
            org.user = user
            org.save()
        except IntegrityError as e:
            messages.error(request, f"{e}")
            return render(request, "create_organization.html")
        return dashboard(request, pk=org.id - 1)
    return render(request, "create_organization.html")


def registration(request):
    form = UserCreation()

    if request.method == 'POST':
        form = UserCreation(request.POST)

        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:
                user = form.save()

                picture = Picture()
                picture.profile_picture = request.FILES.get('file')
                picture.user = user
                picture.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Bot cannot register for this site")
                return render(request, 'register.html')
        context = {"form": form}
        return render(request, 'register.html', context)
    return render(request, 'register.html', {"form":form})


def profile(request, pk):
    return render(request, 'profile.html')


def handle_uploaded_file(f):
    name: str = join(MEDIA_ROOT, 'uploads', gen_new_name(f.name))
    with open(name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def gen_new_name(file_name: str):
    extension = file_name.split(".")[-1]
    return "%s%s.%s" % (time.time_ns(), str(uuid.uuid4()).replace("-", ""), extension)



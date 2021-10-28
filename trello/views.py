# Create your views here.
import time
import requests
import uuid
from os.path import join
from django.contrib.auth.models import User
from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth import login

from django.shortcuts import render, redirect

from Trello import settings
from account.forms import UserCreation
from trello.models import Phone
# Create your views here.


def home(request):
    return render(request, 'home.html')



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

            user = form.save()
            phone = Phone()
            phone.profile_picture = request.FILES.get('file')
            phone.user = user
            phone.save()
            login(request, user)
            return redirect('home')
    context = {"form": form}
    return render(request, 'register.html', context)


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



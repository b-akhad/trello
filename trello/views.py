# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from account.forms import UserCreation
from trello.models import Phone
# Create your views here.


def home(request):
    return render(request, 'home.html')


def registration(request):
    form = UserCreation()

    if request.method == 'POST':
        form = UserCreation(request.POST)
        phone = Phone()
        phone.phone_number = request.POST.get('phone')
        phone.save()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    context = {"form": form}
    return render(request, 'register.html', context)
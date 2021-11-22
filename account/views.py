from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from account.forms import LoginForm
from django.contrib.auth import login, authenticate

from trello.models import Org


def login_redirect(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                active_user = User.objects.get(username=username)
                org = Org.objects.filter(user=active_user)
                org = org[0]
                login(request, user)
                return redirect('dashboard', org.id)
            messages.error(request, 'username or password is incorrect!')
    return render(request, 'login.html', {"form": form})
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailInput



class UserCreation(UserCreationForm):
    email = forms.EmailField(widget=EmailInput(attrs={'class': "form-control", "placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"john"}))

    class Meta:
        model = User
        fields = ("first_name","username", 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'username'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
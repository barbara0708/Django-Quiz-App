from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInfo

class NewUserCreationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","birthday","password1","password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['profile_pic']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserCreationForm(UserCreationForm):
    birthday=forms.DateField()
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=("username","email","birthday","password1","password2")
    def save(self, commit=True):
        user=super(NewUserCreationForm,self).save(commit=True)
        user.email=self.cleaned_data['email']
        user.birthday=self.cleaned_data['birthday']
        if commit:
            user.save()
        return user

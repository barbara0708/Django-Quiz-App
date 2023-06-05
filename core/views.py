from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import NewUserCreationForm


def index(request):
    return render(request,'core/index.html')

def categories(request):
    return render(request,'core/categories.html')

def login_view(request):
    return render(request,'core/login.html')

def signup_view(request):
    if request.method=='POST':
        form=NewUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successful")
            return redirect('login')
        messages.error(request,"Unsuccessful registration. Invalid information.")
    else:
        form=NewUserCreationForm()
    return render(request,'core/registration.html',context={'form':form})
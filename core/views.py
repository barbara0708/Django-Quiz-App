from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import NewUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request,'core/index.html')

def categories(request):
    return render(request,'core/categories.html')

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,"You are logged in now")
            else:    
                messages.error(request,"Invalid email or password")
            return redirect('categories')
        else:
            messages.error(request,"Invalid email or password")
    form=AuthenticationForm()
    return render(request,'core/login.html',context={'login_form':form})

def signup_view(request):
    if request.method=='POST':
        form=NewUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,"Registration successful")
            return redirect('login')
        messages.error(request,"Unsuccessful registration. Invalid information.")
    else:
        form=NewUserCreationForm()
    return render(request,'core/registration.html',context={'form':form})
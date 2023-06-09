from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Categories
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'core/index.html')

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

@login_required
def categories(request):
    all_categories=Categories.objects.all()
    return render(request,'core/categories.html',context={'categories':all_categories})

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
            form.save()
            messages.success(request,"Registration successful")
            return redirect('login')
        messages.error(request,"Unsuccessful registration. Invalid information.")
    else:
        form=NewUserCreationForm()
    return render(request,'core/registration.html',context={'form':form})
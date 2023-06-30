from msilib.schema import ListView
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Categories
from category.models import Scores,Quiz
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'core/index.html')

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

@login_required
def categories(request):
    cat=request.GET.get('search_category')
    if cat is not None:
        all_categories=Categories.objects.filter(name__contains=cat)
    else:
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

def reset_password(request):
    return render(request,'core/reset_password_form.html')

def reset_done(request):
    return render(request,'core/reset_password_done.html')

def reset_complete(request):
    return render(request,'core/reset_password_complete.html')

def reset_confirm(request):
    return render(request,'core/reset_password_confirm.html')

@login_required
def progress(request):
    id=request.user.id
    scores=Scores.objects.filter(user_id=request.user)
    quiz_res={}
    #quizes=Quiz.objects.all()
    for s in scores:
        quiz=Quiz.objects.get(pk=s.quiz_id.id)
        print(type(quiz))
        
        if s.quiz_id not in quiz_res.keys():
            quiz_res[quiz]=[]
            quiz_res[quiz].append(s)
        else:
            quiz_res[quiz].append(s)
        
    return render(request,'core/progress.html',context={'quiz_res':quiz_res})


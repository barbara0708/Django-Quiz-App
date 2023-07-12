from msilib.schema import ListView
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserCreationForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Categories, UserInfo
from category.models import Scores,Quiz
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
from .models import UserInfo

def index(request):
    ids=[]
    quizes=Quiz.objects.all()
    for q in quizes:
        ids.append(q.id)   
    data=[]
    for i in range(4):
        num=random.randint(0,len(ids)-1)
        data.append(Quiz.objects.get(pk=ids[num]))
    return render(request,'core/index.html',context={'data':data})

def profile(request):
    return render(request,'core/profile.html')

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

@login_required
def categories(request):
    opt=True
    return render(request,'core/categories.html',context={'opt':opt})

def search(request):
    cat=request.POST.get('search')
    if cat is not None:
        all_categories=Categories.objects.filter(name__icontains=cat)
    return render(request,'core/search_results.html',context={'categories':all_categories})

def all(request):
    all_categories=Categories.objects.all()
    return render(request,'core/search_results.html',context={'categories':all_categories})


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
        return render(request,'core/login.html',context={'form':form})
    else:
        form=AuthenticationForm()
        return render(request,'core/login.html',context={'form':form})

def signup_view(request):
    if request.method=='POST':
        form=NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            birthday=form.cleaned_data.get('birthday')
            user=User.objects.get(email__exact=email)
            UserInfo.objects.create(user=user,birthday_date=birthday)
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

def upd_info(request):
    id=request.user.id
    scores=Scores.objects.filter(user_id=request.user)
    quiz_res={}
    for s in scores:
        quiz=Quiz.objects.get(pk=s.quiz_id.id)
        if s.quiz_id not in quiz_res.keys():
            quiz_res[quiz]=[]
            quiz_res[quiz].append(s)
        else:
            quiz_res[quiz].append(s)
    return quiz_res

@login_required
def progress(request):
    quiz_res=upd_info(request)
    amount=len(quiz_res)
    form=ProfileForm(request.POST,request.FILES)
    additional_info=UserInfo.objects.get(user=request.user)
    if request.method=='GET':
        return render(request,'core/progress.html',context={'quiz_res':quiz_res,'amount':amount,'info':additional_info,'form':form})

    if request.method=='POST':
        if 'btnChangePicture' in request.POST:
            form=ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success')
            else:
                form=ProfileForm()
            return render(request, 'core/progress', {'form': form,'quiz_res':quiz_res,'amount':amount,'info':additional_info})
        else:
            quiz=request.POST.get('quizID')
            Scores.objects.filter(quiz_id=quiz,user_id=request.user.id).delete()
            quiz_res=upd_info(request)
            return render(request,'core/progress.html',context={'quiz_res':quiz_res,'amount':amount,'info':additional_info})

def success(request):
    pass

def search_view(request):
    pass

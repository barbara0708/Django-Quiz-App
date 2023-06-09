from django.shortcuts import render
from .models import Quiz
from core.models import Categories
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.get(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizes':all_quizes})

@login_required
def quiz(request,slug,id):
    return render(request,'category/quiz.html')

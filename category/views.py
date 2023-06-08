from django.shortcuts import render
from .models import Quiz
from core.models import Categories

# Create your views here.
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.get(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizes':all_quizes})

def quiz(request,slug,id):
    return render(request,'category/quiz.html')

from django.shortcuts import render
from .models import Quiz, Question, Answer
from core.models import Categories
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.filter(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizzes':all_quizes})

@login_required
def quiz(request,url,slug):
    quiz=Quiz.objects.get(url=url)
    questions=Question.objects.filter(quiz_id=quiz.id)
    options=[]
    for q in questions:
        op=Answer.objects.filter(question_id=q.id)
        options.append(op)
    return render(request,'category/quiz.html',context={'quiz':quiz,'questions':questions,'options':options})

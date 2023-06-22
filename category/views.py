from django.shortcuts import render,redirect
from .models import Quiz, Question, Answer
from core.models import Categories
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json

@login_required
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.filter(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizzes':all_quizes})

@login_required
def result(request):
    return render(request,'category/results.html')

@login_required
def quiz(request,url,slug):
    quiz=Quiz.objects.get(url=url)
    questions=Question.objects.filter(quiz_id=quiz.id)
    options=Answer.objects.all()
    paginator=Paginator(questions,1)
    paginator2=Paginator(options,4)
    page_number=request.GET.get('page')
    question=paginator.get_page(page_number)
    op=paginator2.get_page(page_number)
    correct_user_answers=[]
    context={'quiz':quiz,'page_obj':question,'options':op}
    count=0

    if request.method=='GET':
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request,'category/quiz.html',context)

    if request.method=='POST':
        print("Here")
        total_score=0
        right=0
        answers={}
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            data = json.load(request)
            for k,v in data.items():
                if k not in answers.keys():
                    answers[k]=v
                answ=Answer.objects.get(content=v,question__id=k)
                if answ.correct:
                    right+=1
        wrong=len(answers)-right
        total_score=(right/len(answers))*100
        context={'total_score':total_score,'answers':answers,'right':right,'wrong':wrong}  
        print("total score is : ",total_score)          
        return render(request,'category/results.html',context)



    

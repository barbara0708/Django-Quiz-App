from django.shortcuts import render,redirect
from .models import Quiz, Question, Answer,Scores
from core.models import Categories
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from django import db

@login_required
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.filter(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizzes':all_quizes})

@login_required
def result(request):
    print("Finally!")
    return render(request,'category/results.html')

@login_required
def quiz(request,url,slug):
    correct=0
    quiz=Quiz.objects.get(url=url)
    questions=Question.objects.filter(quiz_id=quiz.id)
    options=Answer.objects.all()
    paginator=Paginator(questions,1)
    paginator2=Paginator(options,4)
    page_number=request.GET.get('page')
    question=paginator.get_page(page_number)
    op=paginator2.get_page(page_number)
    context={'page_obj':question,'options':op}
    db.connections.close_all()
    

    if request.method=='GET':
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request,'category/quiz.html',context)

    if request.method=='POST':
        length=int(question.paginator.count)
        answers={}
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            data = json.load(request)
            for k,v in data.items():
                if k not in answers.keys():
                    answers[k]=v
                answ=Answer.objects.get(content=v,question__id=k)
                if answ.correct:
                    correct+=1
        wrong=length-correct
        total_score=(correct/length)*100
        if total_score>75:
            passed=True
        else:
            passed=False
        print("Data to save: ",request.user.id," ",quiz," ",total_score," ",wrong," ",correct)
        Scores.objects.update_or_create(user_id=request.user,quiz_id=quiz,points=total_score,correct=correct,wrong=wrong,passed=passed)
        db.connections.close_all()
    
        return render(request,'category/results.html',context={'wrong':wrong})



    

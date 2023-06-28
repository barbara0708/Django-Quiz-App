from django.shortcuts import render,redirect
from .models import Quiz, Question, Answer,Scores
from core.models import Categories
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from django import db
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.filter(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizzes':all_quizes})

@login_required
def result(request,slug,url):
    ready=False
    user_id=request.user.id
    if request.method=='POST':
        ready=True
        score=Scores.objects.filter(user_id=user_id).latest('quizdate')
        return render(request,'category/results.html',context={'score':score,'ready':ready})
    score=Scores.objects.filter(user_id=user_id).latest('quizdate')
    return render(request,'category/results.html',context={'score':score,'ready':ready})

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
    Scores.objects.update_or_create(user_id=request.user,quiz_id=quiz,points=0,correct=0,wrong=0,passed=False)
    score=Scores.objects.filter(user_id=request.user.id).latest('quizdate')
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
        #Scores.objects.update_or_create(user_id=request.user,quiz_id=quiz,points=total_score,correct=correct,wrong=wrong,passed=passed)
        print("Data to update: quiz_id=",quiz,"points=",total_score,"correct=",correct,"wrong=",wrong,"passed=",passed)
        Scores.objects.filter(pk=score.id).update(quiz_id=quiz,points=total_score,correct=correct,wrong=wrong,passed=passed)
        db.connections.close_all()
        return render(request,'category/quiz.html',context={'score':total_score})



    

from django.shortcuts import render
from .models import Quiz, Question, Answer
from core.models import Categories
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def quizes(request,slug):
    cID=Categories.objects.get(slug=slug)
    all_quizes=Quiz.objects.filter(category_id=cID.id)
    return render(request,'category/quizes.html',context={'quizzes':all_quizes})

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

    if request.method=='GET':
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request,'category/quiz.html',context)

    if request.method=='POST':
        
        user_answer=request.POST['option']
        correct_answers=Answer.objects.filter(correct=True)
        for correct in correct_answers:
            if user_answer == correct.content:
                correct_user_answers.append(user_answer)
                messages.success(request, 'Correct answer')
                print(correct_user_answers)
            return HttpResponseRedirect("?page="+request.session['previous_page'])
        else:
            messages.warning(request, f'Wrong answer, Correct Answer is {correct.content}')
            return HttpResponseRedirect(request.session['previous_page'])
        #return render(request,'category/quiz.html',context)
    
    
    

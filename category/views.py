from django.shortcuts import render
from .models import Quiz, Question, Answer
from core.models import Categories
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
    context={'quiz':quiz,'page_obj':question,'options':op}

    if request.method=='POST':
        correct_user_answers=[]
        user_answer=request.POST['option']
        correct_answers=Answer.objects.filter(correct=True)
        if user_answer in correct_answers:
            correct_user_answers.append(user_answer)
        print(correct_user_answers)
        return render(request,'category/quiz.html',context)
    
    if request.method=='GET':
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request,'category/quiz.html',context)

    

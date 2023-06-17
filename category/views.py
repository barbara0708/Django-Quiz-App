from django.shortcuts import render,redirect
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
def result(request,slug):
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
        print("get request: ")
        request.session['previous_page'] = request.path_info + "?page=" + request.GET.get("page", '1')
        return render(request,'category/quiz.html',context)

    if request.method=='POST':
        print(request.body)
        #parse_json = json.loads(request.body)
        #print(parse_json.items())
        # for k,v in parse_json.items():
        #     ques = QuesModel.objects.get(id=int(k))
        #     answer = v
        #     obj, created = Answer.objects.update_or_create(
        #             ques=ques, answer=answer,  
        #     defaults={'answer': answer, 'examdate': default_date, 'fname': "Bhavesh", "lname": "Patil"})

        return redirect('result')



    

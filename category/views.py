from django.shortcuts import render

# Create your views here.
def quizes(request,slug):
    return render(request,'category/quizes.html')

def quiz(request,slug,id):
    return render(request,'category/quiz.html')

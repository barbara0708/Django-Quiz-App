from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')

def categories(request):
    return render(request,'core/categories.html')
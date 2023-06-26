from django.urls import path, include
from . import views

urlpatterns=[
    path('result/',views.result,name='result'),
    path("<slug:slug>/",views.quizes,name='quizes'),
    path('<slug:slug>/quiz/<slug:url>',views.quiz,name="quiz")
]
from django.urls import path, include
from . import views

urlpatterns=[
    path("<slug:slug>/",views.quizes,name='quizes'),
    path('<slug:slug>/quiz/<slug:url>',views.quiz,name="quiz"),
    path('<slug:slug>/quiz/<slug:url>/result',views.result,name="result")
]
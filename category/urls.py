from django.urls import path, include
from . import views

urlpatterns=[
    path("<slug:slug>/",views.quizes,name='quizes'),
    path('<slug:slug>/quiz/<int:id>',views.quiz,name="categories")
    

]
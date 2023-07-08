from django.db import models
from core.models import Categories
from django.contrib.auth.models import User

class Quiz(models.Model):
    quiz_name=models.CharField(max_length=150,blank=True,null=True)
    desc=models.CharField(max_length=200,blank=True,null=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)
    url=models.SlugField(unique=True,blank=True,null=True)
    img=models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self) :
        return str(self.quiz_name)

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,blank=True,null=True)
    content=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return str(self.content) 

class Scores(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    points=models.IntegerField(null=True)
    correct=models.IntegerField(null=True)
    wrong=models.IntegerField(null=True)
    quizdate=models.DateTimeField(auto_now_add=True)
    passed=models.BooleanField(default=False,null=True)
    def __str__(self):
        return str(self.points) 



class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,blank=True,null=True)
    content=models.CharField(max_length=200,blank=True,null=True)
    correct=models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return str(self.content)


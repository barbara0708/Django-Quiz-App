from django.db import models
from core.models import Categories
from django.contrib.auth.models import User

class Quiz(models.Model):
    quiz_name=models.CharField(max_length=150,blank=True,null=True)
    desc=models.CharField(max_length=200,blank=True,null=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)
    url=models.SlugField(unique=True,blank=True,null=True)
    img=models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self) :
        return str(self.quiz_name)

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,related_name='question',on_delete=models.CASCADE,blank=True,null=True)
    content=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return str(self.content) 

class Scores(models.Model):
    user_id=models.OneToOneField(User,related_name='score',on_delete=models.CASCADE,blank=True,null=True)
    quiz_id=models.OneToOneField(Quiz,related_name='score',on_delete=models.CASCADE,blank=True,null=True)
    points=models.IntegerField(blank=True,null=True)
    correct=models.IntegerField(blank=True,null=True)
    wrong=models.IntegerField(blank=True,null=True)
    passed=models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return str(self.points) 



class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,blank=True,null=True)
    content=models.CharField(max_length=200,blank=True,null=True)
    correct=models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return str(self.content)


from django.db import models
from core.models import Categories
from django.contrib.auth.models import User

class Quiz(models.Model):
    quiz_name=models.CharField(max_length=150)
    desc=models.CharField(max_length=200)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    url=models.SlugField(unique=True)
    def __str__(self) :
        return str(self.quiz_name)

class Question(models.Model):
    quiz=models.OneToOneField(Quiz,related_name='question',on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    def __str__(self):
        return str(self.content) 

class Scores(models.Model):
    user_id=models.OneToOneField(User,related_name='score',on_delete=models.CASCADE)
    quiz_id=models.OneToOneField(Quiz,related_name='score',on_delete=models.CASCADE)
    points=models.IntegerField()

class Answer(models.Model):
    question=models.OneToOneField(Question,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    correct=models.BooleanField(default=False)
    def __str__(self):
        return str(self.content)


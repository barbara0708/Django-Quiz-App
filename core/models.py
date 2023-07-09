from django.db import models
import uuid
from django.contrib.auth.models import User

class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True, default=uuid.uuid1)
    def __str__(self) :
        return str(self.name)

class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,default=uuid.uuid1)
    profile_pic=models.ImageField(upload_to='images/profile_pictures/',blank=True,null=True)
    birthday_date=models.DateField()
    
    def __str__(self) :
        return self.user.username
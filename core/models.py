from django.db import models
import uuid

class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True, default=uuid.uuid1)
    def __str__(self) :
        return str(self.name)
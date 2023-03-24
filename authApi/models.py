from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True,unique=True,auto_created=True,editable=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password=ArrayField(models.CharField(max_length=150),size=10)    
    def __str__(self):
        return self.name
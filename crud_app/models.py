from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=110)
    section=models.CharField(max_length=11)
    age=models.IntegerField()
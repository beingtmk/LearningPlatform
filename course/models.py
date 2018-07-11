from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

class Course(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)   #change this to choice field
    type = models.CharField(max_length=30)      #change this to choice CharField
    instructor = models.CharField(max_length=30)
    #students = models.

    def __str__(self):
        return self.name

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     courses = models.ManyToManyField(Course)

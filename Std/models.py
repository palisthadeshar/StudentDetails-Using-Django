from django.db import models

# Create your models here.
class Student(models.Model):
    MAJOR_CHOICES=(("Chemistry","Chemistry"),("Physics","Physics"),("Biology","Biology"))
    GRADE_CHOICES=(("11","11"),("12","12"))

    name=models.CharField(max_length=60)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=50)
    grade=models.CharField(max_length=5,choices=GRADE_CHOICES)
    major=models.CharField(max_length=20,choices=MAJOR_CHOICES)
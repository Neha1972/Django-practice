from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)


class Student(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=50)
    stuadd = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    teacher_name = models.ForeignKey(Teacher, on_delete=CASCADE, null=True, blank=True)

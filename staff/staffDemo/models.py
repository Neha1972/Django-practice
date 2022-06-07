from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Class_room(models.Model):
    class_room_id = models.IntegerField(primary_key=True)
    class_room_name = models.CharField(max_length=100,blank=True,null=True)

class Student(models.Model):
    student_role_id =models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100,blank=True,null=True)
    student_address = models.CharField(max_length=100,blank=True,null=True)
    student_mobile_no = models.BigIntegerField()
    class_room_id = models.ForeignKey(Class_room ,related_name =  "classRoom",on_delete= CASCADE,blank=True,null=True)	


class Teacher(models.Model):
    teacher_role_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=100,blank=True,null=True)
    teacher_address = models.CharField(max_length=100,blank=True,null=True)
    teacher_mobile_no = models.BigIntegerField()
    class_room_id = models.ForeignKey(Class_room, related_name = "classRoom1",on_delete=CASCADE,blank=True,null=True)	
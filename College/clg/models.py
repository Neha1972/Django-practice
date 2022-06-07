
#Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Class_room(models.Model):
    class_room_id = models.AutoField(primary_key=True)
    class_room_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.class_room_name) 

class Student(models.Model):
    student_role_id =models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100,blank=True,null=True)
    student_address = models.CharField(max_length=100,blank=True,null=True)
    student_mobile_no = models.BigIntegerField()
    class_room_id = models.ForeignKey(Class_room,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
   

class Teacher(models.Model):
    teacher_role_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100,blank=True,null=True)
    teacher_address = models.CharField(max_length=100,blank=True,null=True)
    teacher_mobile_no = models.BigIntegerField()
    class_room_id = models.ForeignKey(Class_room,on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name










        
   
class Details(models.Model):

    class_room_id = models.ForeignKey(Class_room,on_delete=models.CASCADE,default="")
    student_role_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher_role_id = models.ForeignKey(Teacher,on_delete=CASCADE)
     
  


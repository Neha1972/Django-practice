from django.db import models
from django.db.models.fields.related import ManyToManyField
from rest_framework import fields, serializers

from .models import Class_room, Details, Student, Teacher


class Class_room_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Class_room
        #fields = ['class_room_id','class_room_name','student']
        fields = '__all__'


class Student_serilaizer(serializers.ModelSerializer):
  
    #class_room_id = Class_room_serializer(read_only = True)
    class Meta:
        model = Student
        fields = ["student_role_id","student_name","student_address","student_mobile_no","class_room_id"]
        #fields = '__all__'

class Get_Student_serilaizer(serializers.ModelSerializer):
  
    class_room_id = Class_room_serializer(read_only = True)
    class Meta:
        model = Student
        fields = ["student_role_id","student_name","student_address","student_mobile_no","class_room_id"]
        #fields = '__all__'

class Teacher_serializer(serializers.ModelSerializer):


    class Meta:
        model = Teacher
        fields = '__all__'


class Get_Teacher_serializer(serializers.ModelSerializer):

    class_room_id = Class_room_serializer(read_only = True)
    class Meta:
        model = Teacher
        #fields =  ["teacher_role_id","teacher_name","teacher_address","teacher_mobile_no","class_room_id"]
        fields = '__all__'



# class Detail_serializer(serializers.ModelSerializer):
#     class_room_id = Class_room_serializer(read_only = True)
#     student_role_id = Student_serilaizer(read_only=True)
#     teacher_role_id = Teacher_serializer(read_only = True)
#     class Meta:
#          model = Details
#          fields = '__all__'

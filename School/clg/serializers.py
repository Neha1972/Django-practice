from django.db.models.fields.related import ManyToManyField
from .models import Class_room, Student,Teacher
from rest_framework import fields, serializers


class Class_room_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Class_room
        #fields = ['class_room_id','class_room_name','student']
        fields = '__all__'


class Student_serilaizer(serializers.ModelSerializer):
  
    #class_room_id = Class_room_serializer(read_only = True)
    class Meta:
        model = Student
        #fields = ["student_role_id","student_name","student_address","student_mobile_no","class_room_id"]
        fields = '__all__'

class Get_Student_serilaizer(serializers.ModelSerializer):
  
    class_room_id = Class_room_serializer(read_only = True)
    class Meta:
        model = Student
        fields = ["student_role_id","student_name","student_address","student_mobile_no","class_room_id"]
        #fields = '__all__'

class Teacher_serializer(serializers.ModelSerializer):


    class Meta:
        model = Teacher
        #fields =  ["teacher_role_id","teacher_name","teacher_address","teacher_mobile_no","class_room1"]
        fields = '__all__'


class Get_Teacher_serializer(serializers.ModelSerializer):

    class_room_id = Class_room_serializer(read_only = True)
    class Meta:
        model = Teacher
        #fields =  ["teacher_role_id","teacher_name","teacher_address","teacher_mobile_no","class_room_id"]
        fields = '__all__'


   
from django.db import models
from django.db.models import fields
from django.db.models.fields import Field
from .models import Class_room, Student,Teacher
from rest_framework import serializers

class Class_room_serializer(serializers.ModelSerializer):
    class Meta:
        model = Class_room
        fields = "__all__"

class Student_serilaizer(serializers.ModelSerializer):
    classRoom = Class_room
    #classRoom2 =Class_room
    class Meta:
        model = Student
        fields = "__all__"

class Teacher_serializer(serializers.ModelSerializer):
    classRoom1 = Class_room
    #classRoom3 = Class_room
    class Meta:
        models = Teacher
        fields = "__all__"  
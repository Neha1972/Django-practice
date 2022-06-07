from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Employees  
  
  
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Employees
        fields = ("id", "first_name", "last_name")

     

   

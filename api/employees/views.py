from typing import Generic
from django.shortcuts import render
from rest_framework import generics
from .models import Employees
from .serializers import EmployeeSerializer

# Create your views here.
class ListEmployeeView(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializers_class = EmployeeSerializer
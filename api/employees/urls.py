from django.contrib import admin
from django.urls import path,include
from .views import ListEmployeeView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees', views.ListEmployeeView)

urlpatterns = [
    path('employees/',ListEmployeeView.as_view() ,name = "employees-all")
]  
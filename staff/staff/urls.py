"""staff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include 
from django.contrib import admin
from staffDemo.views import create_teacher,create_student,create_classroom,create_student_new,get_student,student_detail,get_student_new
 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('classRoom/',create_classroom),
    path('student/',create_student),
    path('teacher/',create_teacher),
    path('student_1/',create_student_new),
    path('getallstudent/',get_student),
    path('studentdetails/',student_detail)
    #path('getstudent/',get_student_new)
]

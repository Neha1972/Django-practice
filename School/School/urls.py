"""School URL Configuration

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
from django.contrib import admin
from django.urls import path
from clg.views import  create_teacher,create_student,student_get_all,teacher_get_all,get_classRoom,create_classRoom,deleteEdit_classroom, deleteEdit_student, deleteEdit_teacher


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('getclass/',get_classRoom),
    path('createclass/',create_classRoom), 
    path('class/<int:pk>/',deleteEdit_classroom),
   # path('editclass/<int:pk>/',edit_classroom), 
   
   
    path('getstudent/',student_get_all),        
    path('createstudent/',create_student),  
    path('student/<int:pk>/',deleteEdit_student), 
    #path('editstudent/<str:pk>/',edit_student), 
    
   
    path('getteacher/',teacher_get_all),
    path('createteacher/',create_teacher),
    path('teacher/<int:pk>/',deleteEdit_teacher)
    #path("classDetail/",get_class_Details)

    
    
]
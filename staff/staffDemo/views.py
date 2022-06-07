from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Class_room,Student,Teacher
from django.views.decorators.csrf import csrf_exempt
from  staffDemo.serializers import Class_room_serializer, Student_serilaizer,Teacher_serializer
from rest_framework.response import Response
import json

# Create your views here.

@csrf_exempt
def create_classroom(request):
     if request.method == 'GET':
        result = []
        class_r = Class_room.objects.all()
        for cr in class_r:
            data = {
                "class_room_id" : cr.class_room_id,
                "class_room_name" : cr.class_room_name
                    }
            result.append(data)
            #print(result)
        return HttpResponse(json.dumps(result))



     if request.method == "POST":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         class_room_id = data["class_room_id"]
         class_room_name = data["class_room_name"]
         cr = Class_room(class_room_id,class_room_name)
         cr.save()
         return HttpResponse({"classRoom added succesfully"})


     if request.method == "DELETE":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         class_room_id = data["class_room_id"]              
         cr = Class_room.objects.filter(class_room_id=class_room_id).delete()
         return HttpResponse({"ClassRoom deleted succesfully"})

@csrf_exempt
def create_student(request):
     if request.method == 'GET':
        result = []
        student = Student.objects.all()
        for stu in student:
            data = {
                "student_role_id" : stu.student_role_id,
                "student_name" : stu.student_name,
                "student_address" : stu.student_address,
                "student_mobile_no" : stu.student_mobile_no,
                "class_room _id" : stu.class_room_id
            }
            result.append(data)
            #print(result)
        return HttpResponse(json.dumps(result))



     if request.method == "POST":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         student_role_id = data["student_role_id"]
         student_name = data["student_name"]
         student_address = data["student_address"]
         student_mobile_no = data["student_mobile_no"]
         class_room_id = data["class_room_id"]
         stu = Student(student_role_id,student_name,student_address,student_mobile_no,class_room_id)
         stu.save()
         return HttpResponse({"student added succesfully"})

     if request.method == "PUT":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         stu =Student.objects.get()
         data = request.data
         stu.student_role_id = data["student_role_id"]
         stu.save()
         seri = Student_serilaizer(stu)
        
         return HttpResponse({"student data updated succesfully"})


    

     if request.method == "DELETE":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         student_role_id = data["student_role_id"]              
         stu =Student.objects.filter(student_role_id=student_role_id).delete()
         return HttpResponse({"Student deleted succesfully"})
         

@csrf_exempt
def create_teacher(request):
     if request.method == 'GET':
        result = []
        teacher = Teacher.objects.all()
        for tea in teacher:
            data = {
                "teacher_role_id" : tea.student_role_id,
                "teacher_name" : tea.student_name,
                "teacher_address" : tea.student_address,
                "teacher_mobile_no" : tea.student_mobile_no,
                "class_room _id" : tea.class_room_id
            }
            result.append(data)
            #print(result)
        return HttpResponse(json.dumps(result))



     if request.method == "POST":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         teacher_role_id = data["teacher_role_id"]
         teacher_name = data["teacher_name"]
         teacher_address = data["teacher_address"]
         teacher_mobile_no = data["teacher_mobile_no"]
         class_room_id = data["class_room_id"]
         tea = Teacher(teacher_role_id,teacher_name,teacher_address,teacher_mobile_no,class_room_id)
         tea.save()
         return HttpResponse({"teacher added succesfully"})

     if request.method == "PUT":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         tea = Teacher.objects.get()
         data = request.data
         tea.teacher_role_id = data["teacher_role_id"]
         tea.save()
         seri = Teacher_serializer(tea)
         #return Response(seri.data)
         return HttpResponse({"Teacher data updated succesfully"})


    

     if request.method == "DELETE":
         body_unicode = request.body.decode('utf-8')
         data = json.loads(body_unicode)
         teacher_role_id = data["teacher_role_id"]         
         tea =Teacher.objects.filter(teacher_role_id=teacher_role_id).delete()
         return HttpResponse({"Teacher deleted succesfully"})
         



@api_view(["POST"])
def create_student_new(request):
    data = request.data
    seri = Student_serilaizer(data=data)
    if seri.is_valid():
        std_obj = seri.save()
        return Response("sucess")
    return Response(seri.errors)

@api_view(["GET", "POST", "PUT", "DELETE"])
def get_student(request):
    print(request.method)
    pqr = Student.objects.all()
    seri = Student_serilaizer(pqr, many=True)
    return Response(seri.data)

@api_view(["GET"])
def get_student_new(request):
    data = request.data
    pqr = data["student_role_id"]
    student_obj = Student.objects.get(student_role_id=pqr)
    resp = {"student_role_id": student_obj.student_role_id,
            "student_name": student_obj.student_name,
            "student_address": student_obj.student_address,
            "class_room_id": {"class_room_id": student_obj.class_room_id.class_room_id,
                             "class_room_name": student_obj.class_room_id.class_room_name,}}
    return Response(resp)


@api_view(["GET", "POST", "PUT", "DELETE"])
def student_detail(request):
    if request.method == "POST":
        payload = request.data
        abc = Student_serilaizer(data=payload)
        if abc.is_valid():
            student_obj = abc.save()
            return Response(Student_serilaizer(student_obj).data)
        return Response(abc.errors)

    if request.method == "GET":
        data = request.data
        std_obj = Student.objects.get(student_role_id=data["student_role_id"])
        return Response(Student_serilaizer(std_obj).data)

    if request.method == "PUT":
        payload = request.data
        abc = payload["student_role_id"]
        student_obj = Student.objects.get(student_role_id=abc)
        seri = Student_serilaizer(student_obj, data=payload, partial=True)
        if seri.is_valid():
            std_obj = seri.save()
            return Response(seri.data)
        return Response(seri.errors)


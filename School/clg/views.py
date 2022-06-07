from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Class_room,Student,Teacher,Student
from django.views.decorators.csrf import csrf_exempt
from clg.serializers import Class_room_serializer, Student_serilaizer,Teacher_serializer,Get_Student_serilaizer,Get_Teacher_serializer
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])    
def get_classRoom(request):
    if request.method == "GET":
        abc = Class_room.objects.all()
        class_seri = Class_room_serializer(abc, many=True)
        return Response(class_seri.data)
    

@api_view(["POST"])   
def create_classRoom(request):
    data = request.data
    class_seri = Class_room_serializer(data=data)
    if class_seri.is_valid():
        class_obj = class_seri.save()
        return Response("classRoom added succesfully")
    return Response({"error": True, "message": "Unsuccessfull", "response": class_seri.errors}, status=400)

@api_view(["GET","PUT","DELETE"])  
def deleteEdit_classroom(request,pk=None):

     if request.method == "GET":
        try:
            class_room_id = pk
            if class_room_id is not None:
                class_obj = Class_room.objects.get(class_room_id=class_room_id)
                class_seri = Class_room_serializer(class_obj)
                return Response(class_seri.data)

            class_obj = Class_room.objects.all()
            class_seri = Class_room_serializer(class_obj,many=True)
            return Response(class_seri.data)
        except Class_room.DoesNotExist:
            return Response({"error": True, "message": "Unsuccessfull"}, status=400)
            
     if request.method == "DELETE":   
         try:             
            class_seri = Class_room.objects.get(class_room_id=pk).delete()
         except Class_room.DoesNotExist:
            return Response("Invalid Class Room Id")

         return HttpResponse("ClassRoom deleted succesfully")


     if request.method == 'PUT': 
        try:
            class_obj = Class_room.objects.get(class_room_id =pk)
            seri = Class_room_serializer(instance=class_obj,data=request.data)
        except Class_room.DoesNotExist:
            return Response("Invalid class room id")


        if seri.is_valid():
            seri.save()

            return Response("ClassRoom data updated succesfully")

@api_view(["GET"])  
def student_get_all(request):     
      if request.method == "GET":
         try:
             stu_obj = Student.objects.all()
             stu_seri = Get_Student_serilaizer(stu_obj, many=True)
             return Response(stu_seri.data)
         except Student.DoesNotExist:
            return Response({"error": True, "message": "Unsuccessfull"}, status=400)

@api_view(["POST"])
def create_student(request):                       
       if request.method == "POST":
         
        stu_data = JSONParser().parse(request)
        print(stu_data)
        #data = request.data
        student_obj = {"student_role_id": stu_data["student_role_id"],
                        "student_name": stu_data["student_name"],
                         "student_address": stu_data["student_address"],
                         "student_mobile_no": stu_data["student_mobile_no"],
                         "class_room_id": stu_data["class_room_id"]
                         }
        #print(student_obj)
        
        stu_seri = Student_serilaizer(data=student_obj)
        if stu_seri.is_valid():
                 stu_seri.save()
                 return Response("Student added succesfully")
        return Response({"error": True, "message": "Unsuccessfull", "response": stu_seri.errors}, status=400)
 
@api_view(["GET","POST","PUT","DELETE"])  
def deleteEdit_student(request,pk=None):  
     

    if request.method == "GET":
        try:
            student_role_id = pk
            if student_role_id is not None:
                stu_obj= Student.objects.get(student_role_id=student_role_id)
                stu_seri = Student_serilaizer(stu_obj)
                return Response(stu_seri.data)

            stu_obj = Student.objects.all()
            stu_seri = Student_serilaizer(stu_obj,many=True)
            return Response(stu_seri.data)
        except Student.DoesNotExist:
            return Response({"error": True, "message": "Unsuccessfull"}, status=400)



    if request.method == "DELETE":     
      try:
        stu_obj =Student.objects.get(student_role_id=pk).delete()
      except Student.DoesNotExist:

        return Response("invalid student role id")
      return HttpResponse({"student deleted succesfully"})
         

    if request.method == 'PUT': 
      try:
        stu_obj = Student.objects.get(student_role_id =pk)
        stu_seri = Student_serilaizer(instance=stu_obj,data=request.data)
      except Student.DoesNotExist:
          return Response("Invalid student role id")

      if stu_seri.is_valid():
          stu_seri.save()

          return Response("Student data updated succesfully")

@api_view(["GET"])
def teacher_get_all(request):     

     if request.method == "GET":
    
        teacher_obj = Teacher.objects.all()
        teacher_seri = Get_Teacher_serializer(teacher_obj, many=True)
        return Response(teacher_seri.data)

@api_view(["POST"])
def create_teacher(request): 
     if request.method == "POST":
         
        teacher_data = JSONParser().parse(request)
        #print(teacher_data)
        #data = request.data
        student_obj = {"teacher_role_id": teacher_data["teacher_role_id"],
                        "teacher_name": teacher_data["teacher_name"],
                         "teacher_address": teacher_data["teacher_address"],
                         "teacher_mobile_no": teacher_data["teacher_mobile_no"],
                         "class_room_id": teacher_data["class_room_id"]
                         }
        #print(student_obj)
        
        teacher_seri = Student_serilaizer(data=student_obj)
        if teacher_seri.is_valid():
                 teacher_seri.save()
                 return Response("Teacher added succesfully")
        return Response({"error": True, "message": "Unsuccessfull", "response": teacher_seri.errors}, status=400)


@api_view(["GET","POST","DELETE","PUT"])
def deleteEdit_teacher(request,pk=None):
   
    if request.method == "GET":
            try: 
                teacher_role_id = pk
                if teacher_role_id is not None:
                    teacher_obj = Teacher.objects.get(teacher_role_id=teacher_role_id)
                    teacher_seri = Teacher_serializer(teacher_obj)
                    return Response(teacher_seri.data)
                else:
                    teacher_obj= Teacher.objects.all()
                    teacher_seri = Teacher_serializer(teacher_obj,many=True)
                    return Response(teacher_seri.data)

            except Teacher.DoesNotExist:
                return Response({"error": True, "message": "unsuccessfull"}, status=400)

    
    if request.method == "PUT":
        try:
            teacher_obj = Teacher.objects.get(teacher_role_id =pk)
            teacher_seri = Teacher_serializer(instance=teacher_obj,data=request.data)
        except Teacher.DoesNotExist:
            return Response("Invalid Teacher Role Id")
        if teacher_seri.is_valid():
          teacher_seri.save()

        return Response("Teacher data updated succesfully")
           
       
    if request.method == "DELETE":   
        try:             
            teacher_obj = Teacher.objects.get(teacher_role_id=pk).delete()
        except Teacher.DoesNotExist:
            return Response("Invalid Teacher Role Id ")
        return HttpResponse("Teacher deleted succesfully")

#@api_view(["POST"])
# def get_class_Details(request):
#     data = request.data
#     class_room_id = data["class_room_id"]
#     student_role_id = data["student_role_id"]
    
#     stu_id = [x["student_role_id"]for x in student_role_id]
#     stu_obj = Student.objects.filter(class_id = class_room_id, stu_id_id = stu_id).values_list("stu_id_id")
#     stu_list = []
#     for x in student_role_id:
#         if x["student_role_id"] not in stu_obj:
#             stu_list.append(x["student_role_id"])
#     print("output=",stu_list)
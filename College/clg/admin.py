from django.contrib import admin

from clg.models import Class_room, Details, Student, Teacher

# Register your models here.
admin.site.register(Class_room)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Details)

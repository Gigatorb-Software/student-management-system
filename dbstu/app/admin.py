from django.contrib import admin
from . models import *
# Register your models here.


@admin.register((Registration))
class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 'contact']


@admin.register((Course))
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'fees', 'duration', 'comments']


@admin.register((AddStudents))
class AddStudentsModelAdmin(admin.ModelAdmin):
    list_display = ['sname', 'semail', 'smobile', 'saddress',
                    'scollege', 'sdegree', 'scourse', 'total_amount',
                    'paid_amount', 'due_amount']


@admin.register((Teacher))
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['teachername', 'employeesid', 'teacheremail', 'teachermobile', 'joindate',
                    'education', 'workexp', 'photo', 'gender']

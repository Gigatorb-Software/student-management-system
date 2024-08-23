from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from app. models import *
from api.serializers import *

# registration


class RegistrationViewSet(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationShowViewSet(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


# course

class CourseViewSet(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseShowViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteViewSet(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# addstudent


class AddStudentsViewSet(generics.CreateAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer


class AddStudentsShowViewSet(generics.ListAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer


class AddStudentsUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer


class AddStudentsDeleteViewSet(generics.DestroyAPIView):
    queryset = AddStudents.objects.all()
    serializer_class = AddStudentsSerializer
# teacher


class TeacherViewSet(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherShowViewSet(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDeleteViewSet(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

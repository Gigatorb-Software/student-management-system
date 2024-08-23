from rest_framework import serializers
from app.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AddStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddStudents
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(AddStudentsSerializer, self).to_representation(instance)
        rep['scourse'] = instance.scourse.name
        return rep

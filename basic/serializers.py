from rest_framework import serializers
from .models import Skills, Course, RegistrationCourse


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name', 'image']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'iscoursname', 'time', 'duration', 'price', 'created', 'updated', 'skills']


class RegistrationCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCourse
        fields = ['full_name', 'phone_number', 'course']

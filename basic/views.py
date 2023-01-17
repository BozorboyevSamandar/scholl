from rest_framework import serializers, viewsets
from .serializers import SkillsSerializer, CourseSerializer, RegistrationCourseSerializer
from .models import Skills, Course, RegistrationCourse


# Create your views here.


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationCourseViewSet(viewsets.ModelViewSet):
    queryset = RegistrationCourse.objects.all()
    serializer_class = RegistrationCourseSerializer



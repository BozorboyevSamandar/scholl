from django.urls import path, include
from rest_framework import routers

from .views import SkillsViewSet, CourseViewSet, RegistrationCourseViewSet

router = routers.DefaultRouter()

router.register('skills', SkillsViewSet)
router.register('course', CourseViewSet)
router.register('register_course', RegistrationCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

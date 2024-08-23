from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .api import *
urlpatterns = [
    path('reg/', RegistrationViewSet.as_view()),
    path('regshow/', RegistrationShowViewSet.as_view()),
    path('course/', CourseViewSet.as_view()),
    path('courseshow/', CourseShowViewSet.as_view()),
    path('courseupdate/<int:pk>/', CourseUpdateViewSet.as_view()),
    path('coursedelete/<int:pk>/', CourseDeleteViewSet.as_view()),
    path('addstu/', AddStudentsViewSet.as_view()),
    path('stushow/', AddStudentsShowViewSet.as_view()),
    path('stuupdate/<int:pk>/', AddStudentsUpdateViewSet.as_view()),
    path('studelete/<int:pk>/', AddStudentsDeleteViewSet.as_view()),
    path('addtech/',TeacherViewSet.as_view()),
    path('techshow/', TeacherShowViewSet.as_view()),
    path('techupdate/<int:pk>/', TeacherUpdateViewSet.as_view()),
    path('techdelete/<int:pk>/', TeacherDeleteViewSet.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

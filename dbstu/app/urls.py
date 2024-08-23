from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
urlpatterns = [
    path('', views.index),
    path('courses/', views.courses),
    path('dashboard/', views.dashboard),
    path('signup/', views.signup),
    path('viewstudents/', views.viewstudents),
    path('registration/', views.registration),
    path('login/', views.login),
    path('addcourse/', views.addcourse),
    path('update_view/<int:uid>/', views.update_view, name='Updatecourse'),
    path('updatecourse/', views.updatecourse),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('update_student/', views.update_student),
    path('updatestu/<int:uid>/', views.updatestu),
    path('teacher/', views.teacher),
    path('addteacher/', views.addteacher),
    path('updatetech/<int:uid>/', views.updatetech),
    path('update_teacher/', views.update_teacher),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete, name="delete"),
    path('logout/', views.logout),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

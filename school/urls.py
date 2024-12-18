from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_student/', views.login_student, name='login_student'),
    path('login_teacher/', views.login_teacher, name='login_teacher'),
    path('grades/', views.grades, name='grades'),
    path('upload_grades/', views.upload_grades, name='upload_grades'),
]

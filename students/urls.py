from django.urls import path
from . import views

urlpatterns = [
    path('student_list/', views.readStudent, name='student_list'),
    path('create_student/', views.createStudent, name='create_student'),
]
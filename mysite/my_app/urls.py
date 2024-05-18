from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('courses/', views.course_list, name='course_list'),  # Course list page
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),  # Course detail page
    path('register/', views.student_registration, name='student_registration'),  # Student registration page
]


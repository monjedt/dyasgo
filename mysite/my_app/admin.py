

# Register your models here.
from django.contrib import admin
from .models import Student, Course, CourseSchedule, StudentReg

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseSchedule)
admin.site.register(StudentReg)

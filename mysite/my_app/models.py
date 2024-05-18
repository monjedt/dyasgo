from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    days = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course.name} - {self.days}"

class StudentReg(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"

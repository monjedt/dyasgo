from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Student, Course, CourseSchedule, StudentReg

class StudentModelTest(TestCase):
    def test_string_representation(self):
        student = Student(name="John Doe")
        self.assertEqual(str(student), student.name)

from django.shortcuts import get_object_or_404, render

from my_app.models import Course

def index(request):
    return render(request, 'index.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def student_registration(request):
    if request.method == 'POST':
        # Handle registration logic here
        pass
    return render(request, 'student_registration.html')

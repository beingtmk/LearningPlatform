from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from django.urls import reverse_lazy

#Models import
from .models import User, Course, Student

# Create your views here.
# def index(request):
#     return HttpResponse("You're looking at the Courses HomePage!")

class CourseListView(ListView):
    model = Course

def enroll(request, course_id):
    if request.user.is_authenticated:

        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            student = Student(user=request.user)

        student.save()
        student.courses.add(Course.objects.get(id=course_id))
        student.save()

        return redirect('courses_enrolled')
        # return HttpResponse(Course.objects.get(id=course_id).name)
    else:
        return redirect("account_login")

def unenroll(request, course_id):
    student = Student.objects.get(user=request.user)
    student.courses.remove(Course.objects.get(id=course_id))
    student.save()

    return redirect('courses_enrolled')

# class EnrolledListView(ListView):
#     template_name = "course/enrolled_list.html"
#     context_object_name = 'course_list'
#
#     def enrolled_list(request):
#         """Return the last five published matches."""
#         return Student.objects.get(user=request.user).courses

def enrolled_list(request):
    course_list = Student.objects.get(user=request.user).courses
    context = {'course_list': course_list}
    return render(request, "course/enrolled_list.html", context)

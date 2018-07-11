from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

#Models import
from .models import Course

# Create your views here.
# def index(request):
#     return HttpResponse("You're looking at the Courses HomePage!")

class CourseListView(ListView):

    model = Course

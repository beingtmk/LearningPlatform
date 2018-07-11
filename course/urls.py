from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course_index"),

]

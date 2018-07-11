from django.urls import include, path
from . import views

urlpatterns = [
    path("list", views.CourseListView.as_view(), name="course_list"),
    path("list/<int:course_id>/enroll/", views.enroll, name="course_enroll"),
    path("list/<int:course_id>/unenroll/", views.unenroll, name="course_unenroll"),
    path("list/enrolled", views.enrolled_list, name="courses_enrolled"),

]

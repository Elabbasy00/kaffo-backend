from src.education.views import EducationView, EducationLevelView, GradeCoursesView, GetSingleCourse, EducationStages
from django.urls import path


urlpatterns = [
    path("", EducationView.as_view(), name="education"),
    path("stages/", EducationStages.as_view(), name="stages"),
    path("levels/", EducationLevelView.as_view(), name="levels"),
    path("grade-courses/", GradeCoursesView.as_view(), name="grade-courses"),
    path("single-course/", GetSingleCourse.as_view(), name="single-course"),
]

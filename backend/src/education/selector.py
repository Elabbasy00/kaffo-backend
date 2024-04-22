from src.education.models import Education, Course, Video, EducationLevel, EducationStage
from src.common.utils import get_object


class EducationRepository:
    @staticmethod
    def get_education_list():
        return Education.objects.all()

    @staticmethod
    def filter_education_stages(*args, **kwargs):
        return EducationStage.objects.filter(*args, **kwargs)

    @staticmethod
    def get_education_levels(*, education_stage: str | int):
        return EducationLevel.objects.filter(education_stage__slug=education_stage)


class CoursesRepository:
    @staticmethod
    def get_courses_list():
        return Course.objects.all().select_related("grade_level")

    @staticmethod
    def get_grade_courses(*, grade: str | int):
        return Course.objects.filter(grade_level__slug=grade)

    @staticmethod
    def get_single_course(*, slug: str | int):
        return get_object(Course.objects.prefetch_related("course_videos"), slug=slug)

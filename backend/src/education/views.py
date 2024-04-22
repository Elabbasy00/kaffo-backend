from rest_framework import serializers, response, status, views
from src.education.selector import EducationRepository, CoursesRepository
from src.api.utils import inline_serializer
from src.education.services import get_education_stages


class EducationView(views.APIView):

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        image = serializers.ImageField()
        slug = serializers.SlugField()

    def get(self, request):
        educations = EducationRepository.get_education_list()
        serializer = self.OutputSerializer(educations, many=True, context={"request": request}).data

        return response.Response(serializer)


class EducationStages(views.APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        slug = serializers.SlugField(allow_unicode=True)
        image = serializers.ImageField()
        grade_levels = inline_serializer(
            fields={"id": serializers.CharField(), "name": serializers.CharField(), "slug": serializers.SlugField()},
            many=True,
        )

    def get(self, request):
        slug = request.GET.get("slug")
        stages = get_education_stages(education_slug=slug)
        serializer = self.OutputSerializer(stages, context={"request": request}, many=True).data
        return response.Response(serializer)


class EducationLevelView(views.APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        slug = serializers.SlugField()

    def get(self, request):
        stage = request.GET.get("stage")
        educations = EducationRepository.get_education_stages(education=stage)
        serializer = self.OutputSerializer(educations, many=True, context={"request": request}).data

        return response.Response(serializer)


class GradeCoursesView(views.APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        slug = serializers.SlugField(allow_unicode=True)
        title = serializers.CharField(max_length=150)
        subject = serializers.CharField(max_length=200)
        desc = serializers.CharField()
        cover = serializers.ImageField()

    def get(self, request):
        grade = request.GET.get("grade_level")
        courses = CoursesRepository.get_grade_courses(grade=grade)
        serializers = self.OutputSerializer(courses, many=True, context={"request": request}).data
        return response.Response(serializers)


class GetSingleCourse(views.APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        slug = serializers.SlugField(allow_unicode=True)
        title = serializers.CharField(max_length=150)
        subject = serializers.CharField(max_length=200)
        desc = serializers.CharField()
        cover = serializers.ImageField()
        course_videos = inline_serializer(
            fields={
                "id": serializers.CharField(),
                "title": serializers.CharField(),
                "link": serializers.URLField(),
                "cover": serializers.ImageField(),
                "is_trial": serializers.BooleanField(default=False),
            },
            many=True,
        )

    def get(self, request):
        slug = request.GET.get("slug")
        course = CoursesRepository.get_single_course(slug=slug)
        serializer = self.OutputSerializer(course, context={"request": request}).data
        return response.Response(serializer)

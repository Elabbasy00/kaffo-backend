from django.db import models
from django.core.validators import URLValidator
from django_resized import ResizedImageField


class Education(models.Model):
    name = models.CharField(max_length=50)
    image = ResizedImageField(size=[500, 500], force_format="WEBP", quality=100, upload_to="stage/")
    slug = models.SlugField(allow_unicode=True, unique=True)

    def __str__(self):
        return self.name


class EducationStage(models.Model):
    education_stage = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="educationـstage")
    image = ResizedImageField(
        size=[500, 500], force_format="WEBP", quality=100, upload_to="educationـstage/", null=True, blank=True
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    educationـgrade = models.ForeignKey(
        EducationStage, on_delete=models.SET_NULL, null=True, blank=True, related_name="grade_levels"
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    grade_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, related_name="course_for")
    slug = models.SlugField(allow_unicode=True, unique=True)
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    desc = models.TextField()
    cover = models.ImageField(upload_to="courses/covers/")

    def __str__(self) -> str:
        return self.title


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_videos")
    title = models.CharField(max_length=150, null=True, blank=True)
    link = models.TextField(validators=[URLValidator()])
    cover = models.ImageField(upload_to="courses/videos/covers/")
    is_trial = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

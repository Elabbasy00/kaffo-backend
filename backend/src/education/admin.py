from django.contrib import admin
from src.education.models import Education, EducationLevel, Course, Video, EducationStage


class LevelInline(admin.StackedInline):
    model = EducationLevel
    prepopulated_fields = {"slug": ["name"]}


class VideoInline(admin.StackedInline):
    model = Video


@admin.register(EducationLevel)
class EducationStageAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationStage)
class EducationStageAdmin(admin.ModelAdmin):
    inlines = [LevelInline]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Education)
class EducationalStageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    prepopulated_fields = {"slug": ["title"]}

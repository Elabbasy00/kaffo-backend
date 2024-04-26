from django.contrib import admin
from src.services.models import Project, ProjectGallery, Service


class InlineProject(admin.StackedInline):
    model = Project
    # prepopulated_fields = {"slug": ["title"]}


class ProjectGalleryInline(admin.StackedInline):
    model = ProjectGallery


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    inlines = [InlineProject]

    prepopulated_fields = {"slug": ["title"]}


@admin.register(Project)
class ProjectAdmim(admin.ModelAdmin):
    inlines = [ProjectGalleryInline]

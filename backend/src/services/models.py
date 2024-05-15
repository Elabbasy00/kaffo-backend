from django.db import models
from django_resized import ResizedImageField

SERVICE_PARENT = (("coding", "Coding"), ("market", "Market"))


class Service(models.Model):
    title = models.CharField(max_length=100)
    cover = ResizedImageField(size=[300, 200], force_format="WEBP", quality=100, upload_to="services/cover/")
    slug = models.SlugField(allow_unicode=True, unique=True)
    parent = models.CharField(choices=SERVICE_PARENT, max_length=10)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="project_for")
    title = models.CharField(max_length=100)
    cover = ResizedImageField(
        force_format="WEBP", size=[500, 500], quality=100, upload_to="services/projects/", null=True, blank=True
    )
    overview = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    img = ResizedImageField(force_format="WEBP", size=[500, 500], quality=100, upload_to="services/projects/")

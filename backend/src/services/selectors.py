from src.services.models import Service, Project


def get_services():
    return Service.objects.all()


def get_services_projects(*, slug: str):
    return Project.objects.filter(service__slug=slug).prefetch_related("gallery")

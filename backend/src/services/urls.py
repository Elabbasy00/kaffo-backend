from src.services.views import GetServices, GetServicesPerParent
from django.urls import path


urlpatterns = [
    path("", GetServices.as_view(), name="all-services"),
    path("service-detail/", GetServicesPerParent.as_view(), name="service-detail"),
]

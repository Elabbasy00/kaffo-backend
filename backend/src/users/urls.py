from django.urls import path
from src.users.views import ContactUsView

urlpatterns = [path("contact-us/", ContactUsView.as_view(), name="contact-us")]

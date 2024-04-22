from src.users.models import ContactUs


class ContactUsRepository:
    @staticmethod
    def create_contact_us(*args, **kwargs):
        return ContactUs.objects.create(*args, **kwargs)

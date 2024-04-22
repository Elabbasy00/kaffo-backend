from rest_framework import views, serializers, response, status
from src.users.selector import ContactUsRepository


class ContactUsView(views.APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=200)
        email = serializers.EmailField()
        phone_number = serializers.CharField(max_length=200)
        service = serializers.CharField(max_length=300)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ContactUsRepository.create_contact_us(**serializer.validated_data)
        return response.Response({"message": "استلامنا طلبك و سنقوم برد عليك في اقرب وقت"})

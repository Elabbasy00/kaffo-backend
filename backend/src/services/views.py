from rest_framework import status, serializers, response, views
from src.services.selectors import get_services, get_services_projects
from src.api.utils import inline_serializer


class GetServices(views.APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        title = serializers.CharField()
        cover = serializers.ImageField()
        slug = serializers.SlugField(allow_unicode=True)
        parent = serializers.CharField()

    def get(self, request):
        services = get_services()
        serializers = self.OutputSerializer(services, many=True, context={"request": request}).data
        return response.Response(serializers)


class GetServicesPerParent(views.APIView):
    class InputSerializer(serializers.Serializer):
        slug = serializers.SlugField(allow_unicode=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        title = serializers.CharField()
        cover = serializers.ImageField()
        overview = serializers.CharField()
        gallery = inline_serializer(fields={"img": serializers.ImageField()}, many=True)

    def get(self, request):
        input_data = self.InputSerializer(data=request.GET)
        input_data.is_valid(raise_exception=True)
        services = get_services_projects(slug=input_data.validated_data.get("slug"))

        serializers = self.OutputSerializer(services, many=True, context={"request": request}).data
        return response.Response(serializers)

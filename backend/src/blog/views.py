from src.api.pagination import LimitOffsetPagination, get_paginated_response
from rest_framework import views, status, response, serializers
from src.blog.selector import BlogRepository
from src.api.serializers import FixAbsolutePathSerializer


class GetPostsViews(views.APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        cover = serializers.ImageField()
        overview = serializers.CharField()
        created_at = serializers.DateTimeField()
        content = FixAbsolutePathSerializer()
        slug = serializers.SlugField(allow_unicode=True)

    def get(self, request):
        queryset = BlogRepository.get_all_post()
        # serializers = self.OutputSerializer(queryset, many=True, context={"request": request})
        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=queryset,
            request=request,
            view=self,
        )


class GetSinglePostView(views.APIView):
    class InputSerializer(serializers.Serializer):
        slug = serializers.SlugField(allow_unicode=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        cover = serializers.ImageField()
        overview = serializers.CharField()
        created_at = serializers.DateTimeField()
        content = FixAbsolutePathSerializer()
        slug = serializers.SlugField(allow_unicode=True)

    def get(self, request):
        input_data = self.InputSerializer(data=request.GET)
        input_data.is_valid(raise_exception=True)

        post = BlogRepository.get_single_post(slug=input_data.validated_data.get("slug"))
        serializer = self.OutputSerializer(post, context={"request": request}).data
        return response.Response(serializer)

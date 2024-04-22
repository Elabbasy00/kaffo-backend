# from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )
from src.users.selectors import user_get_login_data
from src.api.mixins import ApiAuthMixin
from src.users.services import user_create
from django.contrib.auth.password_validation import validate_password


class UserRegister(APIView):
    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        email = serializers.EmailField()
        username = serializers.CharField()
        password = serializers.CharField()

    def post(self, request):
        data = request.data
        print("data", request.data)
        serializer = self.InputSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validate_password(serializer.validated_data.get("password"))
        user_create(**serializer.validated_data)
        return Response({"hi"})


class UserSessionLoginApi(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is None:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        data = user_get_login_data(user=user)
        session_key = request.session.session_key

        return Response({"session": session_key, "data": data})


class UserSessionLogoutApi(ApiAuthMixin, APIView):
    def get(self, request):
        logout(request)

        return Response()

    def post(self, request):
        logout(request)

        return Response()


# class UserJwtLoginApi(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         # We are redefining post so we can change the response status on success
#         # Mostly for consistency with the session-based API
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == status.HTTP_201_CREATED:
#             response.status_code = status.HTTP_200_OK

#         if settings.SIMPLE_JWT["JWT_AUTH_COOKIE"] is not None:
#             response.set_cookie(
#                 key=settings.SIMPLE_JWT["JWT_AUTH_COOKIE"],
#                 value=response.data.get("access"),
#                 expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
#                 secure=settings.SIMPLE_JWT["JWT_AUTH_COOKIE_SECURE"],
#                 samesite=settings.SIMPLE_JWT["JWT_AUTH_COOKIE_SAMESITE"],
#             )

#         return response


# class UserJwtLogoutApi(ApiAuthMixin, APIView):
#     def post(self, request):

#         response = Response()

#         if settings.SIMPLE_JWT["JWT_AUTH_COOKIE"] is not None:
#             response.delete_cookie(settings.SIMPLE_JWT["JWT_AUTH_COOKIE"])

#         return response


class UserMeApi(ApiAuthMixin, APIView):
    def get(self, request):
        data = user_get_login_data(user=request.user)

        return Response(data)

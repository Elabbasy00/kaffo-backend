from dj_rest_auth.serializers import LoginSerializer, PasswordResetSerializer
from rest_framework import serializers
from src.authentication.forms import CustomAllAuthPasswordResetForm


class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = None


class CustomUserDetailsSerializer(serializers.Serializer):
    id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_admin = serializers.BooleanField()
    is_superuser = serializers.BooleanField()


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomAllAuthPasswordResetForm

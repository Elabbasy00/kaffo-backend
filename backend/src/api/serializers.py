from rest_framework import serializers
from django.conf import settings
from config.env import env

SEARCH_PATTERN = 'src="/media/uploads/'


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):

        text = value.replace(SEARCH_PATTERN, settings.REPLACE_WITH)

        return text

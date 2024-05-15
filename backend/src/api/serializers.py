from rest_framework import serializers
from django.conf import settings


SEARCH_PATTERN = 'src="/media/uploads/'


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):

        text = value.replace(SEARCH_PATTERN, settings.REPLACE_WITH)

        return text

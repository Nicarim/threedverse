from rest_framework import serializers

from object_storage.models import VerseProject


class VerseProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseProject
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')

from rest_framework import serializers

from object_storage.models import VerseProject, VerseImage, VerseObject


class VerseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseImage
        fields = ('id', 'name', 'image')


class VerseObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseObject
        fields = ('id', 'name', 'group_id', 'file')
        read_only = ('group_id',)


class VerseProjectSerializer(serializers.ModelSerializer):
    verse_objects = VerseObjectSerializer(many=True, read_only=True)
    images = VerseImageSerializer(many=True, read_only=True)

    class Meta:
        model = VerseProject
        fields = ('id', 'name', 'description', 'verse_objects', 'images', 'created_at', 'updated_at')

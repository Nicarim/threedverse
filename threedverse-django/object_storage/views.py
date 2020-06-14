from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from object_storage.models import VerseProject, VerseImage
from object_storage.serializers import VerseProjectSerializer, VerseImageSerializer, VerseObjectSerializer


class VerseProjectViewSet(viewsets.ModelViewSet):
    queryset = VerseProject.objects.all()
    serializer_class = VerseProjectSerializer

    @action(detail=True, methods=['post'])
    def add_verse_object(self, request, **kwargs):
        project: VerseProject = self.get_object()
        verse_object_serializer = VerseObjectSerializer(data=request.data)
        verse_object_serializer.is_valid(True)
        verse_object = verse_object_serializer.save()
        project.verse_objects.add(verse_object)
        project.save()
        return Response({'status': 'ok'})

    @action(detail=True, methods=['post'])
    def add_image(self, request, **kwargs):
        project: VerseProject = self.get_object()
        image_serializer = VerseImageSerializer(data=request.data)
        image_serializer.is_valid(True)
        image: VerseImage = image_serializer.save()
        image.verse_project = project
        image.save()
        return Response({'status': 'ok'})

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from object_storage.models import VerseProject, VerseImage
from object_storage.serializers import VerseProjectSerializer, VerseImageSerializer


class VerseProjectViewSet(viewsets.ModelViewSet):
    queryset = VerseProject.objects.all()
    serializer_class = VerseProjectSerializer

    @action(detail=True, methods=['post'])
    def add_image(self, request, **kwargs):
        project: VerseProject = self.get_object()
        image_serializer = VerseImageSerializer(data=request.data)
        image_serializer.is_valid(True)
        image: VerseImage = image_serializer.save()
        image.verse_project = project
        image.save()
        return Response({'status': 'ok'})

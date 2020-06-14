from rest_framework import viewsets

from object_storage.models import VerseProject
from object_storage.serializers import VerseProjectSerializer


class VerseProjectViewSet(viewsets.ModelViewSet):
    queryset = VerseProject.objects.all()
    serializer_class = VerseProjectSerializer


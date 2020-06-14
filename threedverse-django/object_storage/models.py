import hashlib
import uuid

from django.db import models

from core.models import BaseAppModel

BUF_SIZE = 65536


class VerseObject(BaseAppModel):
    name = models.CharField(max_length=2048)
    group_id = models.UUIDField(default=uuid.uuid4)
    version = models.CharField(max_length=255, blank=True)
    file = models.FileField(null=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        sha1 = hashlib.sha1()

        while True:
            data = self.file.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
        self.version = str(sha1.hexdigest())
        super().save(force_insert, force_update, using, update_fields)


class VerseProject(BaseAppModel):
    name = models.CharField(max_length=2048)
    description = models.TextField(default='')

    verse_objects = models.ManyToManyField(VerseObject)


class VerseImage(BaseAppModel):
    verse_project = models.ForeignKey(VerseProject, on_delete=models.CASCADE, related_name="images", null=True,
                                      default=None)
    verse_object = models.ForeignKey(VerseObject, on_delete=models.CASCADE, related_name="visualizations", null=True,
                                     default=None)
    name = models.CharField(default='', max_length=255)
    image = models.ImageField()

from django.db import models
from django.utils import timezone


class BaseAppModel(models.Model):
    created_at = models.DateTimeField(verbose_name="When object was first created", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="When object was last updated (any of its values)", auto_now=True)

    class Meta:
        abstract = True

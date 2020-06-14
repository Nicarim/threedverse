from rest_framework import routers

from object_storage import views

router = routers.DefaultRouter()
router.register(r'projects', views.VerseProjectViewSet)

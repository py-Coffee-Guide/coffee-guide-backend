
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.cafe import CafeViewSet

app_name = "api"

router = DefaultRouter()

router.register(
    "cafe", CafeViewSet, basename="cafe"
)


urlpatterns = [
    path("v1/", include(router.urls)),
]

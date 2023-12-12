from api.views.cafe import (
    CafeViewSet,
    CityViewSet,
    ContactViewSet,
    DistrictViewSet,
    PointViewSet,
    ScheduleViewSet,
    StopFactorViewSet,
)
from api.views.reviews import ReciewViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet

app_name = "api"

router = DefaultRouter()

router.register(
    "cafe",
    CafeViewSet,
    basename="cafe",
)
router.register("attributs", StopFactorViewSet)
router.register("contacts", ContactViewSet)
router.register("points", PointViewSet)
router.register("city", CityViewSet)
router.register("district", DistrictViewSet)
router.register("schedule", ScheduleViewSet)
router.register("reviews", ReciewViewSet)
router.register("city", CityViewSet)
router.register("users", CustomUserViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
]

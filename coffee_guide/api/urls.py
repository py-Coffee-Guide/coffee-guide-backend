from api.views.cafe import (
    CafeViewSet,
    # CityViewSet,
    # ContactViewSet,
    # DistrictViewSet,
    # MetroViewSet,
    # PointViewSet,
    # ScheduleViewSet,
    # StopFactorViewSet,
)
from api.views.reviews import ReviewViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet

app_name = "api"

router = DefaultRouter()

router.register("cafe", CafeViewSet, basename="cafe")
# router.register("attributes", StopFactorViewSet, basename="attributes")
# router.register("contacts", ContactViewSet, basename="contacts")
# router.register("points", PointViewSet, basename="points")
# router.register("city", CityViewSet, basename="city")
# router.register("district", DistrictViewSet, basename="district")
# router.register("schedule", ScheduleViewSet, basename="schedule")
router.register(
    r"cafe/(?P<cafe_id>\d+)/reviews",
    ReviewViewSet,
    basename="reviews",
)
# router.register(r"metro", MetroViewSet, basename="metro")
router.register("users", CustomUserViewSet, basename="users")


urlpatterns = [
    path("v1/auth/", include("djoser.urls.authtoken")),
    path("v1/", include(router.urls)),
]

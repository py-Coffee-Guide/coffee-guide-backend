from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views.cafe import (
    AlternativeViewSet,
    CafeViewSet,
    AddressViewSet,
    TagViewSet,
    RoasterViewSet,
    DrinkViewSet,
    ScheduleViewSet)
from users.views import CustomUserViewSet

router = DefaultRouter()

router.register(r"cafe", CafeViewSet, basename="cafes")
router.register(r"addresses", AddressViewSet, basename="addresses")
router.register(r"additionals", AlternativeViewSet, basename="additionals")
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"roasters", RoasterViewSet, basename="roasters")
router.register(r"drinks", DrinkViewSet, basename="drinks")
router.register(r"schedules", ScheduleViewSet, basename="schedules")
router.register("users", CustomUserViewSet, basename="users")


urlpatterns = [
    path("v1/auth/", include("djoser.urls.authtoken")),
    path("v1/", include(router.urls)),
]

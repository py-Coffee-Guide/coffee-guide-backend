from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views.cafe import CafeViewSet
from users.views import CustomUserViewSet

app_name = "api"

router = DefaultRouter()

router.register(r"cafes", CafeViewSet, basename="cafes")
router.register("users", CustomUserViewSet, basename="users")


urlpatterns = [
    path("v1/auth/", include("djoser.urls.authtoken")),
    path("v1/", include(router.urls)),
]

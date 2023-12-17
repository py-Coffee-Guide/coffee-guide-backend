from django.shortcuts import render
from djoser.views import UserViewSet
from django.contrib.auth import login
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from social_django.utils import psa


def auth(request):
    print(request)
    return render(request, "auth.html")


@extend_schema(tags=["Users"], description="Администратор")
@extend_schema_view(
    list=extend_schema(summary="Список пользователей", methods=["GET"]),
    # retrieve=extend_schema(
    #     summary="Детальная информация о пользователе (id=номер телефона)",
    #     methods=["GET"],
    # ),
)
class CustomUserViewSet(UserViewSet):
    """
    Вьюсет для:

    - изменения пароля;
    - изменения username;
    - регистрации нового пользователя;
    """

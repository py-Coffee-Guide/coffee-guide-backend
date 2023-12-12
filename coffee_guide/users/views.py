from djoser.views import UserViewSet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)


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

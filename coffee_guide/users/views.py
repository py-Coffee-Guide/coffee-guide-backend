from djoser.views import UserViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .backends import get_cofirmation_code, get_phone_data


class CustomUserViewSet(UserViewSet):
    """
    Вьюсет для:

    - изменения пароля;
    - изменения username;
    - регистрации нового пользователя;
    """

    @action(
        detail=False,
        methods=("GET", "POST"),
        url_path="phone_registration",
    )
    def phone_registration(self, request) -> Response:
        """
        Функция для регистрации по номеру телефона.
        """
        if request.method == "POST":
            return get_cofirmation_code(self, request)
        else:
            return get_phone_data(self, request)

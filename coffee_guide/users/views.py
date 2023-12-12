from djoser.views import UserViewSet


class CustomUserViewSet(UserViewSet):
    """
    Вьюсет для:

    - изменения пароля;
    - изменения username;
    - регистрации нового пользователя;
    """

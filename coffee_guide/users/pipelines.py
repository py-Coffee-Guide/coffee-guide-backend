from .models import CustomUser
from rest_framework import status
from rest_framework.serializers import ValidationError


def save_user_vk(backend, user, response, *args, **kwargs):
    """Функция для сохранения данных из ВКонтакте для кастомной модели юзера."""
    if backend.name == 'vk-oauth2':
        print(response)
        vk_id = response.get('id')
        username = response.get('name')
        email = response.get('email')
        # access_token = response.get("access_token")
        try:
            user, created = CustomUser.objects.get_or_create(
                id=vk_id,
                username=username,
                email=email
            )
        except Exception:
            raise ValidationError(status=status.HTTP_400_BAD_REQUEST,
                                  detail="Неверные данные!")

        return {'user': user}


def save_user_github(backend, user, response, *args, **kwargs):
    """Функция для сохранения данных из GitHub для кастомной модели юзера."""
    if backend.name == 'github':
        # print(response)
        git_id = response.get('id')
        username = response.get('name')
        email = response.get('email')
        # access_token = response.get("access_token")
        # print(username, email, access_token)

        try:
            user, created = CustomUser.objects.get_or_create(
                id=git_id,
                username=username,
                email=email
            )
        except Exception:
            raise ValidationError(status=status.HTTP_400_BAD_REQUEST,
                                  detail="Неверные данные!")

        return {'user': user}

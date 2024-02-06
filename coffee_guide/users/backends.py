import json
import random

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser


class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id) -> CustomUser | None:
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None

    def authenticate(self, request, username, password) -> CustomUser | None:
        try:
            user: CustomUser = CustomUser.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )

        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        else:
            return None


# def get_cofirmation_code(self, request) -> Response:
#     """ "
#     Функция принимающая на входно номер телефона, пароль и
#     проверочный код. После сверки кода и данных на телефон,
#     сохраняет пользователя в БД.
#     """
#     phone: str = request.data.get("phone")
#     password: str = request.data.get("password")
#     confirmation_code: str = request.data.get("confirmation_code")
#     with open("./users/data/phone_data.json", "r") as f:
#         phone_data: json = json.load(f)
#     if phone_data[phone] != confirmation_code:
#         return Response(
#             {"error": "Неверный проверочный код! Повторите попытку"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
#     data: dict[str, str] = {"phone": phone, "password": password}
#     print(request.data)
#     serializer = OnlyPhoneSerializer(data=data, context={"request": request})
#     serializer.is_valid(raise_exception=True)
#     CustomUser.objects.create_user(phone=phone, password=password)
#     return Response(serializer.data)


# def get_phone_data(self, request) -> Response:
#     """Функция для получения проверочного кода.
#     Функция принимает номер телефона, генерирует код и заносит
#     в JSON файл. После отправляет код потдверждения.
#     """
#     phone = request.data.get("phone")
#     with open("./users/data/phone_data.json", "r") as f:
#         data = json.load(f)
#     serializer = OnlyPhoneSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     confirmation_code = random.randint(1000, 9999)
#     data[phone] = confirmation_code
#     with open("./users/data/phone_data.json", "w") as f:
#         json.dump(data, f)
#     return Response(
#         {"confirmation_code": confirmation_code}, status=status.HTTP_200_OK
#     )


# reddis для confirmation_code.

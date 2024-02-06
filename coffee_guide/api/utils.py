import random

from api.serializers.cafe import CafeUserSerializer
from dadata import Dadata
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from users.models import CustomUser

from coffee_guide.settings import CHARS, SECRET, TOKEN


# def add_to(self, model, user, pk) -> Response:
#     """Добавить заведение."""
#     if model.objects.filter(user=user, cafe__id=pk).exists():
#         return Response(
#             {"errors": "Заведение уже добавлено!"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
#     try:
#
#         cafe = get_object_or_404(model, id=pk)
#     except ObjectDoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
#     model.objects.create(user=user, cafe=cafe)
#     serializer = CafeUserSerializer(cafe)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
def add_to(self, model, user, pk) -> Response:
    """Добавить заведение."""
    if model.objects.filter(user=user, cafe__id=pk).exists():
        return Response(
            {"errors": "Заведение уже добавлено!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        cafe = get_object_or_404(model, id=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        created_object = model.objects.create(user=user, cafe=cafe)
        serializer = CafeUserSerializer(created_object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def delete_from(self, model, user, pk) -> Response:
    """Удалить заведение."""
    cafe = get_object_or_404(model, id=pk)
    obj = model.objects.filter(user=user, cafe=cafe).first()
    if obj:
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(
        {"errors": "Заведение не найдено для удаления!"},
        status=status.HTTP_400_BAD_REQUEST,
    )


def check_inn(organization_inn):
    """Проверка ИНН с помощью сервиса DaData."""
    dadata = Dadata(TOKEN, SECRET)
    result = dadata.find_by_id(name="party", query=organization_inn)
    if not result:
        raise ValidationError("ИНН не существует.")


def password_generation():
    """Генерация пароля."""

    password = ""
    for i in range(9):
        password += random.choice(CHARS)

    return password

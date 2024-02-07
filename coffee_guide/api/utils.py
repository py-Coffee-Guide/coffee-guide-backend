import random

from dadata import Dadata
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from users.models import CustomUser

from coffee_guide.settings import CHARS, SECRET, TOKEN
# from api.serializers.cafe import CafeUserSerializer
# from django.core.exceptions import ObjectDoesNotExist
import base64

from rest_framework import serializers
# from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile


# from cafe.models import Drink, DrinkInCafe, Schedule, ScheduleInCafe

# from rest_framework import status
# from rest_framework.response import Response



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


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
        return super().to_internal_value(data)


# def create_drinks(
#         drinks,
#         instance,
# ):
#     DrinkInCafe.objects.bulk_create(
#         [
#             DrinkInCafe(
#                 cafe=instance,
#                 drink=get_object_or_404(
#                     Drink, id=drink_data["id"]
#                 ),
#                 cost=drink_data["cost"]
#             )
#             for drink_data in drinks
#         ]
#     )


# def create_schedules(
#         schedules,
#         instance,
# ):
#     ScheduleInCafe.objects.bulk_create(
#         [
#             ScheduleInCafe(
#                 cafe=instance,
#                 schedules=get_object_or_404(
#                     Schedule, id=schedules_data["schedules"].id
#                 ),
#                 start=schedules_data["start"],
#                 end=schedules_data["end"]
#             )
#             for schedules_data in schedules
#         ]
#     )



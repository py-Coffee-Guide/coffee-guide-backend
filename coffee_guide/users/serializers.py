from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import exceptions as django_exceptions
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    username = serializers.CharField(
        required=False,
        validators=[UnicodeUsernameValidator()],
    )

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "phone",
            "password",
        )


# class SetPasswordSerializer(serializers.Serializer):
#     """Изменение пароля пользователя."""

#     current_password = serializers.CharField()
#     new_password = serializers.CharField()

#     def validate(self, obj):
#         try:
#             validate_password(obj["new_password"])
#         except django_exceptions.ValidationError as error:
#             raise serializers.ValidationError(
#                 {"new_password": list(error.messages)}
#             )
#         return super().validate(obj)

#     def update(self, instance, validated_data):
#         if not instance.check_password(validated_data["current_password"]):
#             raise serializers.ValidationError(
#                 {"current_password": "Неверный пароль."}
#             )
#         if (
#             validated_data["current_password"]
#             == validated_data["new_password"]
#         ):
#             raise serializers.ValidationError(
#                 {"new_password": "Введите новый пароль."}
#             )
#         instance.set_password(validated_data["new_password"])
#         instance.save()
#         return validated_data


# class SetUsernameSerializer(serializers.Serializer):
#     """Изменение username пользователя."""

#     current_password = serializers.CharField()
#     new_username = serializers.CharField(
#         validators=[UnicodeUsernameValidator()]
#     )

#     def validate(self, obj):
#         if not obj["new_username"]:
#             raise serializers.ValidationError(
#                 {"new_username": "Новый username не может быть пустым."}
#             )

#         return super().validate(obj)

#     def update(self, instance, validated_data):
#         if not instance.check_password(validated_data["current_password"]):
#             raise serializers.ValidationError(
#                 {"current_password": "Неверный пароль."}
#             )
#         instance.username = validated_data["new_username"]
#         instance.save()

#         return validated_data

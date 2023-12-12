from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError as DjangoValidationError
from djoser.serializers import (
    SetPasswordSerializer,
    SetUsernameSerializer,
    UserCreateSerializer,
    UserSerializer,
)
from rest_framework import serializers
from users.models import CustomUser


class CustomUserCreateByEmailSerializer(UserCreateSerializer):
    """Сериализатор для регистрации по email."""

    registration_type = serializers.CharField(default="email")
    username = serializers.CharField(
        required=False,
        validators=[UnicodeUsernameValidator()],
    )
    email = serializers.EmailField(required=True)

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "registration_type", "username", "email", "password")

    # Сделать с валидацией вместо двух отдельных


class CustomUserCreateByPhoneSerializer(UserCreateSerializer):
    """Сериализатор для регистрации по phone."""

    # добавил поле registration_type для определения какой
    # способ регистрации используется
    registration_type = serializers.CharField(default="phone")
    username = serializers.CharField(
        required=False,
        validators=[UnicodeUsernameValidator()],
    )
    phone = serializers.CharField(required=True)

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "registration_type", "username", "phone", "password")


class ConfirmationCodeSerializer(serializers.Serializer):
    """Сериализатор для отправки confirmation_code."""

    confirmation_code = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ("confirmation_code", )


class CustomUserLoginByEmailSerializer(UserSerializer):
    """Сериализатор для входа по email."""

    login_type = serializers.CharField(default="email")
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ("login_type", "email", "password")


class CustomUserLoginByPhoneSerializer(UserSerializer):
    """Сериализатор для входа по phone."""

    login_type = serializers.CharField(default="phone")
    phone = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ("login_type", "phone", "password")


class CustomSetPasswordSerializer(SetPasswordSerializer):
    """Сериализатор для изменение пароля пользователя."""

    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, data):
        current_password = data.get("current_password", "")
        new_password = data.get("new_password", "")

        try:
            validate_password(new_password)
        except DjangoValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)}
            )

        user = self.context["request"].user
        if not user.check_password(current_password):
            raise serializers.ValidationError(
                {"current_password": ["Текущий пароль введен неверно."]}
            )

        return super().validate(data)

    def update(self, instance, validated_data):
        if not instance.check_password(validated_data["current_password"]):
            raise serializers.ValidationError(
                {"current_password": "Неверный пароль."}
            )
        if (
            validated_data["current_password"]
            == validated_data["new_password"]
        ):
            raise serializers.ValidationError(
                {"new_password": "Введите новый пароль."}
            )
        instance.set_password(validated_data["new_password"])
        instance.save()
        return validated_data


class CustomSetUsernameSerializer(SetUsernameSerializer):
    """Сериализатор для изменение username пользователя."""

    current_password = serializers.CharField()
    new_username = serializers.CharField(
        validators=[UnicodeUsernameValidator()]
    )

    def validate(self, data):
        new_username = data.get("new_username")

        if not new_username:
            raise serializers.ValidationError(
                {"new_username": "Новый username не может быть пустым."}
            )

        return super().validate(data)

    def update(self, instance, validated_data):
        if not instance.check_password(validated_data["current_password"]):
            raise serializers.ValidationError(
                {"current_password": "Неверный пароль."}
            )
        instance.username = validated_data["new_username"]
        instance.save()

        return validated_data

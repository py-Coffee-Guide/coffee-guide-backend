from djoser.serializers import (
    UserCreateSerializer,
    UserSerializer,
)
from rest_framework import serializers
from users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(max_length=50, required=False)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "email",
            "password",
        )


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = CustomUser
        fields: tuple = (
            'id',
            'first_name',
            'username',
            'email',
            'phone',
        )


class OnlyPhoneSerializer(UserCreateSerializer):
    "Сериализатор для регистрации только по телефону."
    phone = serializers.CharField(max_length=11)

    class Meta:
        model = CustomUser
        fields = (
            "phone",
            "password",
        )

    def validate(self, attrs):
        phone = attrs.get("phone")
        if CustomUser.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("Этот номер телефона уже зарегестрирован!")
        return attrs

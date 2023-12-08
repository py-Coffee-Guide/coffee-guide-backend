from rest_framework import serializers
from reviews.models import Review
from users.models import User


class SmallUserSerializer(serializers.ModelSerializer):
    """Сериализация данных: Данные пользователя для отзывов"""

    class Meta:
        model = User
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация данных: Отзывы"""

    establishment = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )
    author = SmallUserSerializer(read_only=True)

    class Meta:
        fields = "__all__"
        model = Review

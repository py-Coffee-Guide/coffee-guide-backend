from rest_framework import serializers
from reviews.models import Review

# from users.models import CustomUser

# TODO: Протестить, потом удалить коменты
# class SmallUserSerializer(serializers.ModelSerializer):
#     """Сериализация данных: Данные пользователя для отзывов"""
#
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
#


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация данных: Отзывы"""

    def validate_score(self, value):
        """Дополнительная валидация на уровне сериализатора"""
        if value not in range(1, 6):
            raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
        return value

    class Meta:
        model = Review
        fields = ("id", "cafe", "author", "score", "pub_date")
        read_only_fields = ("pub_date",)

    # cafe = serializers.SlugRelatedField(
    #     slug_field="name",
    #     read_only=True,
    # )
    # author = SmallUserSerializer(read_only=True)
    #
    # class Meta:
    #     fields = "__all__"
    #     model = Review

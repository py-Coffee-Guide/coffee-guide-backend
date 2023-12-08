from rest_framework import serializers

from ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """Сериализация данных: Рейтинг"""


    class Meta:
        model = Rating
        fields = '__all__'

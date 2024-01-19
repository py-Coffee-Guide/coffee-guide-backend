from ...cafe.models import (
    Cafe,
    Schedule,
    Roaster,
    Tag,
    Drink,
    ImageCafe
)
from rest_framework import serializers


class DrinkSerializer(serializers.ModelSerializer):
    """Сериализация данных: Напитков."""

    class Meta:
        model = Drink
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    """Сериализация данных: Время работы."""

    class Meta:
        model = Schedule
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    """Сериализация данных: Тэгов."""

    class Meta:
        model = Tag
        fields = "__all__"


class RoasterSerializer(serializers.ModelSerializer):
    """Сериализация данных: Обжарщиков."""

    class Meta:
        model = Roaster
        fields = "__all__"


class ImageCafeSerializer(serializers.ModelSerializer):
    """Сериализация данных: Картинок."""

    class Meta:
        model = ImageCafe
        fields = ("image_url", )


class CafeSerializer(serializers.ModelSerializer):
    """Сериализация данных: Кофейня"""
    schedule = ScheduleSerializer(many=True, read_only=True)
    roaster = RoasterSerializer(many=True, read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    drink = DrinkSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = ImageCafe.objects.filter(cafe=obj)
        if image.exists():
            return image.first().image_url
        else:
            return None

    class Meta:
        model = Cafe
        fields = (
            "id",
            "name",
            "description",
            "district",
            "address",
            "latitude",
            "longitude",
            # "poster",
            "schedule",
            "filter",
            "alternative",
            "roaster",
            "tag",
            "drink",
            "image"
        )


class CafeUserSerializer(serializers.ModelSerializer):
    """Сериализация данных: Карточка кофейни"""

    class Meta:
        model = Cafe
        fields = ("id", "name", "address", "poster")

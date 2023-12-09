from rest_framework import serializers
from cafe.models import (
    Cafe,
    City,
    Contact,
    District,
    Point,
    Schedule,
    StopFactor,
)


class CafeSerializer(serializers.ModelSerializer):
    """Сериализация данных: Кофейня"""

    class Meta:
        model = Cafe
        fields = "__all__"


class CafeUserSerializer(serializers.ModelSerializer):
    """Сериализация данных: Карточка кофейни"""

    class Meta:
        model = Cafe
        fields = ("id", "name", "address", "poster")


class StopFactorSerializer(serializers.ModelSerializer):
    """Сериализация данных: Доп. свойства"""

    class Meta:
        model = StopFactor
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Сериализация данных: Контакты"""

    class Meta:
        model = Contact
        fields = "__all__"


class PointSerializer(serializers.ModelSerializer):
    """Сериализация данных: Координаты"""

    class Meta:
        model = Point
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    """Сериализация данных: Город"""

    class Meta:
        model = City
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    """Сериализация данных: Район"""

    class Meta:
        model = District
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    """Сериализация данных: Время работы"""

    class Meta:
        model = Schedule
        fields = "__all__"

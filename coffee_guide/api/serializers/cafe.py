from api.utils import Base64ImageField, create_drinks, create_schedules
from users.serializers import CustomUserSerializer

from cafe.models import (
    Cafe,
    DrinkInCafe,
    # ImageCafe,
    Schedule,
    Roaster,
    ScheduleInCafe,
    Tag,
    Drink,
    Address,
    Alternative
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


class AddressSerializer(serializers.ModelSerializer):
    """Сериализация данных: Адрес."""

    class Meta:
        model = Address
        fields = "__all__"


class AlternativeSerializer(serializers.ModelSerializer):
    """Сериализация данных: Доп.опции."""
    class Meta:
        model = Alternative
        fields = "__all__"


class RoasterSerializer(serializers.ModelSerializer):
    """Сериализация данных: Обжарщиков."""

    class Meta:
        model = Roaster
        fields = "__all__"


class DrinkInCafeGetSerializer(serializers.ModelSerializer):
    """Сериализация данных: Напитки в кофейне get."""
    id = serializers.ReadOnlyField(source="drink.id")
    name = serializers.CharField(source="drink.name")

    class Meta:
        model = DrinkInCafe
        fields = ("id", "name", "cost")


class DrinkInCafeCreateSerializer(serializers.ModelSerializer):
    """Сериализация данных: Напитки в кофейне post."""

    id = serializers.IntegerField(write_only=True)
    # id = serializers.PrimaryKeyRelatedField(
    #     source="drink",
    #     queryset=Drink.objects.all()
    # )
    class Meta:
        model = DrinkInCafe
        fields = ("id", "cost")


class ScheduleInCafeGetSerializer(serializers.ModelSerializer):
    """Сериализация данных: Расписание в кофейне get."""
    id = serializers.ReadOnlyField(source="schedules.id")
    name = serializers.CharField(source="schedules.name")

    class Meta:
        model = ScheduleInCafe
        fields = ("id", "name", "start", "end")

class ScheduleInCafeCreateSerializer(serializers.ModelSerializer):
    """Сериализация данных: Расписание в кофейне post."""
    id = serializers.PrimaryKeyRelatedField(
        source="schedules",
        queryset=Schedule.objects.all()
    )
    class Meta:
        model = ScheduleInCafe
        fields = ("id", "start", "end")

# class ImageCafeSerializer(serializers.ModelSerializer):
#     """Сериализация данных: Картинок."""
#     image_file = Base64ImageField()

#     class Meta:
#         model = ImageCafe
#         fields = ('image_file',)

class CafeGetSerializer(serializers.ModelSerializer):
    "Гет сериализатор кофеен"
    schedules = ScheduleInCafeGetSerializer(many=True, read_only=True, source="schedule_in_cafe")
    alternatives = AlternativeSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    roasters = RoasterSerializer(many=True, read_only=True)
    drinks = DrinkInCafeGetSerializer(many=True, read_only=True, source="drink")
    organization = CustomUserSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Cafe
        fields = (
            "id",
            "name",
            "description",
            "schedules",
            "alternatives",
            "address",
            "roasters",
            "tags",
            "drinks",
            "image",
            "organization"
        )

    # def get_image_file(self, obj):
    #     images = obj.image.all()
    #     serializer = ImageCafeSerializer(
    #         images, many=True, read_only=True
    #     )
    #     return serializer.data
    

class CafeCreateSerializer(serializers.ModelSerializer):
    """Пост сериализатор кофеен"""
    schedules = ScheduleInCafeCreateSerializer(many=True)
    drinks = DrinkInCafeCreateSerializer(many=True)
    # address = AddressSerializer()
    # roasters = RoasterSerializer(many=True)
    image = Base64ImageField()

    class Meta:
        model = Cafe
        fields = (
            "id",
            "name",
            "description",
            "schedules",
            "alternatives",
            "address",
            "roasters",
            "tags",
            "drinks",
            "image",
            "organization"
        )

    def create(self, validated_data):
        schedules = validated_data.pop("schedules")
        drinks = validated_data.pop("drinks")
        image = validated_data.pop("image")
        instance = super().create(validated_data)
        create_schedules(schedules, instance)
        create_drinks(drinks, instance)
        create_image(image, instance)
        
        return instance

    def update(self, instance, validated_data):
        schedules = validated_data.pop("schedules")
        drinks = validated_data.pop("drinks")
        image = validated_data.pop("image")
        instance.schedules.clear()
        instance.drinks.clear()
        super().update(instance, validated_data)
        create_schedules(schedules, instance)
        create_drinks(drinks, instance)
        create_image(image, instance)
        instance.save()
        return instance

    def to_representation(self, instance):
        request = self.context.get("request")
        context = {"request": request}
        return CafeGetSerializer(instance, context=context).data
    

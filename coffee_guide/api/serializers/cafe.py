from rest_framework import serializers
from cafe.models import Establishment

class CafeSerializer(serializers.ModelSerializer):
    """Сериализация данных: Заведение"""

    class Meta:
        model = Establishment
        fields = '__all__'

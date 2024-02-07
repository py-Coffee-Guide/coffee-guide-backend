from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import CafeFilter
from api.serializers.cafe import (
    AlternativeSerializer,
    CafeCreateSerializer,
    CafeGetSerializer,
    DrinkSerializer,
    ScheduleSerializer,
    TagSerializer,
    AddressSerializer,
    RoasterSerializer,
)
# from api.utils import add_to, delete_from
from cafe.models import (
    Alternative,
    Cafe,
    Address,
    Tag,
    Roaster,
    Drink,
    Schedule,
)
from drf_spectacular.utils import (
    # OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@extend_schema(
    tags=["Кофейня"],
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список заведений",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о заведении",
    ),
    create=extend_schema(
        summary="Создать заведение",
    ),
    update=extend_schema(
        summary="Обновить заведение",
    ),
    partial_update=extend_schema(
        summary="Частичное обновление заведения",
    ),
    destroy=extend_schema(
        summary="Удалить заведение",
    ),
)
class CafeViewSet(viewsets.ModelViewSet):
    """Вьюсет: Кофейня"""
    queryset = Cafe.objects.all()
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ['name', 'address']
    # filterset_class = CafeFilter
    # /api/cafe/?ordering=district

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return CafeGetSerializer
        return CafeCreateSerializer
    
    def perform_create(self, serializer):
        return serializer.save(organization=self.request.user)


@extend_schema(
    tags=["Адрес"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список адресов",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об адресе",
    ),
)
class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

@extend_schema(
    tags=["Альтернатива"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список альтернатив",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об альтернативе",
    ),
)
class AlternativeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer

@extend_schema(
    tags=["Теги"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список тегов",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о тегах",
    ),
)
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@extend_schema(
    tags=["Обжарщик"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список обжарщиков",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об обжарщике",
    ),
)
class RoasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer

@extend_schema(
    tags=["Напитки"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список напитков",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о напитке",
    ),
)
class DrinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

@extend_schema(
    tags=["Время работы"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список расписания работы",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о расписании работы",
    ),
)
class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer



# @extend_schema(
#     tags=["Кофейня"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Стоп фактор",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о заведении",
#     ),
# )
# class StopFactorViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет: Доп. свойство"""

#     queryset = StopFactor.objects.all()


# @extend_schema(
#     tags=["Кофейня"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Контакты",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о заведении",
#     ),
# )
# class ContactViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет: Контактов"""

#     queryset = Contact.objects.all()


# @extend_schema(
#     tags=["Кофейня"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Координаты",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о заведении",
#     ),
# )
# class PointViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет: Координатов"""

#     queryset = Point.objects.all()


# @extend_schema(
#     tags=["Адрес"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Город",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о городе",
#     ),
# )
# class CityViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет: Городов"""

#     queryset = City.objects.all()


# @extend_schema(
#     tags=["Адрес"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Район",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о районе",
#     ),
# )
# class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет: Районов"""

#     queryset = District.objects.all()


# @extend_schema(
#     tags=["Адрес"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Метро",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о метро",
#     ),
# )
# class MetroViewSet(viewsets.ModelViewSet):
#     """Вьюсет: Метро"""

#     queryset = Metro.objects.all()
#     serializer_class = MetroSerializer


# @extend_schema(
#     tags=["Кофейня"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Время работы",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о времени работы",
#     ),
# )
# class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет: Времени работы"""

#     queryset = Schedule.objects.all()


# @extend_schema(
#     tags=["Отзывы"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Отзывы",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация об отзыве",
#     ),
# )
# class EventUsersViewSet(viewsets.ModelViewSet):
#     """Вьюсет: Отзывы(пользователь)"""

#     pass

#     serializer_class = EventSerializer
#     http_method_names = ["get"]

#     def get_queryset(self):
#         establishment_id = self.kwargs.get("establishment_id")
#         establishment = get_object_or_404(Establishment, id=establishment_id)
#         return establishment.event.all()

#     def perform_create(self, serializer):
#         establishment_id = self.kwargs.get("establishment_id")
#         establishment = get_object_or_404(Establishment, id=establishment_id)
#         serializer.save(establishment=establishment)

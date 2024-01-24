from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import CafeFilter
from api.serializers.cafe import CafeCreateSerializer, CafeGetSerializer
# from api.utils import add_to, delete_from
from cafe.models import (
    Cafe,
    # City,
    # Contact,
    # District,
    # Favorite,
    # Metro,
    # Point,
    # Schedule,
    # StopFactor,
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


# @extend_schema(
#     tags=["Кофейня"],
#     methods=["GET"],
#     description="Все пользователи",
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Получить список заведений",
#     ),
#     retrieve=extend_schema(
#         summary="Детальная информация о заведении",
#     ),
# )
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


    # @action(
    #     detail=True,
    #     methods=["POST", "DELETE"],
    #     permission_classes=(IsAuthenticated,),
    # )
    # def favorite(self, request, pk) -> Response:
    #     """Работа с избранным добавить/удалить"""
    #     if request.method == "POST":
    #         return add_to(self, Favorite, request.user, pk)
    #     else:
    #         return delete_from(self, Favorite, request.user, pk)

    # queryset = Cafe.objects.filter(is_verified=True)
    # # filterset_class = CafeFilter
    # pagination_class = LargeResultsSetPagination
    # permission_classes = (ReadOnly | IsAdminUser,)
    # search_fields = (
    #     "$name",
    #     "$address",
    # )
    # serializer_class = CafeSerializer
    # http_method_names = ["get"]


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

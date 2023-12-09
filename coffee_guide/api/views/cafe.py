# from drf_spectacular.utils import (
#     extend_schema,
#     extend_schema_view,
#     OpenApiParameter,
# )
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from api.utils import add_to, delete_from

from cafe.models import (
    Cafe,
    City,
    Contact,
    District,
    Favorite,
    Point,
    Schedule,
    StopFactor,
)


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
class CafeViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Кофейня"""

    queryset = Cafe.objects.all()

    @action(
        detail=True,
        methods=["POST", "DELETE"],
        permission_classes=(IsAuthenticated,),
    )
    def favorite(self, request, pk) -> Response:
        """Работа с избранным добавить/удалить"""
        if request.method == "POST":
            return add_to(self, Favorite, request.user, pk)
        else:
            return delete_from(self, Favorite, request.user, pk)

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


class StopFactorViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Доп. свойство"""

    queryset = StopFactor.objects.all()


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Контактов"""

    queryset = Contact.objects.all()


class PointViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Координатов"""

    queryset = Point.objects.all()


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Городов"""

    queryset = City.objects.all()


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Районов"""

    queryset = District.objects.all()


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет: Времени работы"""

    queryset = Schedule.objects.all()


# @extend_schema(
#     tags=["События"],
#     methods=["GET", "POST", "PATCH", "DELETE"],
# )
# @extend_schema_view(
#     list=extend_schema(
#         summary="Получить список событий к заведению с id=",
#         description="Клиент/ресторатор",
#     ),
# )
class EventUsersViewSet(viewsets.ModelViewSet):
    """Вьюсет: Отзывы(пользователь)"""

    pass

    # serializer_class = EventSerializer
    # http_method_names = ["get"]
    #
    # def get_queryset(self):
    #     establishment_id = self.kwargs.get("establishment_id")
    #     establishment = get_object_or_404(Establishment, id=establishment_id)
    #     return establishment.event.all()
    #
    # def perform_create(self, serializer):
    #     establishment_id = self.kwargs.get("establishment_id")
    #     establishment = get_object_or_404(Establishment, id=establishment_id)
    #     serializer.save(establishment=establishment)

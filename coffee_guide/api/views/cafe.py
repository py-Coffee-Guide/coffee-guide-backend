# from drf_spectacular.utils import (
#     extend_schema,
#     extend_schema_view,
#     OpenApiParameter,
# )
from rest_framework import viewsets


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
    pass

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

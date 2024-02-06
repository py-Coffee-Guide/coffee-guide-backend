# from api.serializers.cafe import CafeUserSerializer
# from django.core.exceptions import ObjectDoesNotExist
# import base64

# from rest_framework import serializers
# from django.shortcuts import get_object_or_404
# from django.core.files.base import ContentFile


# from cafe.models import Drink, DrinkInCafe, Schedule, ScheduleInCafe

# from rest_framework import status
# from rest_framework.response import Response


# # def add_to(self, model, user, pk) -> Response:
# #     """Добавить заведение."""
# #     if model.objects.filter(user=user, cafe__id=pk).exists():
# #         return Response(
# #             {"errors": "Заведение уже добавлено!"},
# #             status=status.HTTP_400_BAD_REQUEST,
# #         )
# #     try:
# #
# #         cafe = get_object_or_404(model, id=pk)
# #     except ObjectDoesNotExist:
# #         return Response(status=status.HTTP_400_BAD_REQUEST)
# #
# #
# #     model.objects.create(user=user, cafe=cafe)
# #     serializer = CafeUserSerializer(cafe)
# #     return Response(serializer.data, status=status.HTTP_201_CREATED)
# def add_to(self, model, user, pk) -> Response:
#     """Добавить заведение."""
#     if model.objects.filter(user=user, cafe__id=pk).exists():
#         return Response(
#             {"errors": "Заведение уже добавлено!"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
#     try:
#         cafe = get_object_or_404(model, id=pk)
#     except ObjectDoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     try:
#         created_object = model.objects.create(user=user, cafe=cafe)
#         serializer = CafeUserSerializer(created_object)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# def delete_from(self, model, user, pk) -> Response:
#     """Удалить заведение."""
#     cafe = get_object_or_404(model, id=pk)
#     obj = model.objects.filter(user=user, cafe=cafe).first()
#     if obj:
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     return Response({"errors": "Заведение не найдено для удаления!"}, status=status.HTTP_400_BAD_REQUEST)


# class Base64ImageField(serializers.ImageField):
#     def to_internal_value(self, data):
#         if isinstance(data, str) and data.startswith("data:image"):
#             format, imgstr = data.split(";base64,")
#             ext = format.split("/")[-1]
#             data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
#         return super().to_internal_value(data)


# def create_drinks(
#         drinks,
#         instance,
# ):
#     DrinkInCafe.objects.bulk_create(
#         [
#             DrinkInCafe(
#                 cafe=instance,
#                 drink=get_object_or_404(
#                     Drink, id=drink_data["id"]
#                 ),
#                 cost=drink_data["cost"]
#             )
#             for drink_data in drinks
#         ]
#     )


# def create_schedules(
#         schedules,
#         instance,
# ):
#     ScheduleInCafe.objects.bulk_create(
#         [
#             ScheduleInCafe(
#                 cafe=instance,
#                 schedules=get_object_or_404(
#                     Schedule, id=schedules_data["schedules"].id
#                 ),
#                 start=schedules_data["start"],
#                 end=schedules_data["end"]
#             )
#             for schedules_data in schedules
#         ]
#     )


# def create_image(
#         image,
#         instance,
# ):
#     print(image)
#     ImageCafe.objects.create(cafe=instance, image_file=image["image_file"])

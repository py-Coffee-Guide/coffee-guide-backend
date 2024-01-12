from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from django.utils.html import format_html

from .models import (
    Cafe,
    Filter,
    Schedule,
    Alternative,
    Roaster,
    Tag,
    Drink,
    ImageCafe
)

# # from django.utils.safestring import mark_safe


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    """Админка: Заведение"""

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = (
        "id",
        "name",
        "description",
        "district",
        "address",
        "latitude",
        "longitude"
    )
    list_filter = (
        "name",
        "address",
        # "stop_factors"
    )

    search_fields = ['name', 'address']

    fieldsets = (
        ("Основная информация",
            {"fields": (
                # "id",
                "name",
                "description",
                "district",
                "poster"
            )}),
        (
            "Контакты и адреса",
            {"fields": (
                "address",
                # "contact",
                "latitude",
                "longitude")},
        ),
    )
    # list_filter = ("name",)
    # empty_value_display = "-пусто-"
    # autocomplete_fields = ["cities"]

    # def preview(self, obj):
    #     """Отображение превью заведения"""
    #     if obj.poster:
    #         return mark_safe(
    #             f'<img src="{obj.poster.url}" style="max-height: 50px;">'
    #         )
    #     else:
    #         return "No preview"

    # preview.short_description = "Превью"


@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Alternative)
class AlternativeAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("text", )


# @admin.register(ImageCafe)
# class ImageCafeAdmin(admin.ModelAdmin):
#     list_display = (
#         "image_tag",
#         "image_file",
#         "image_url"
#     )
#     readonly_fields = ("image_tag",)

#     def image_tag(self, obj):
#         return format_html(
#             '<img src="{}" width="100" height="100" />'.format
#             (obj.image_file.url)
#         )

#     image_tag.short_description = "Картинка"
#     image_tag.allow_tags = True


# @admin.register(Point)
# class PointAdmin(admin.ModelAdmin):
#     """Админка: Координаты"""

#     list_display = (
#         "lat",
#         "lon"
#     )


# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     """Админка: Контакты"""

#     list_display = (
#         "id",
#         "phone",
#         "website",
#         "email"
#         )
#     list_filter = ("website",)

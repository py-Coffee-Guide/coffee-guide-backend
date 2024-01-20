from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
# from django.utils.html import format_html

from .models import (
    Address,
    Additional,
    Cafe,
    Schedule,
    ScheduleInCafe,
    Roaster,
    Tag,
    Drink,
    DrinkInCafe,
    ImageCafe
)

# # from django.utils.safestring import mark_safe


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    """Админка: Заведение"""

    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }

    list_display = (
        "id",
        "name",
        "description",
        "organization"
    )
    list_filter = (
        "name",
        "organization",
    )
    filter_horizontal = (
        "schedulesincafe",
        "additionals",
        "roasters",
        "tags",
        "drinks"
    )

    search_fields = ['name',]

    fieldsets = (
        ("Основная информация",
            {"fields": (
                # "id",
                "name",
                "description",
                "organization"
            )}),
        # (
        #     "Контакты и адреса",
        #     {"fields": (
        #         "address")},
        # ),
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


@admin.register(ImageCafe)
class ImageCafeAdmin(admin.ModelAdmin):
    list_display = ("cafe", "image_file", "image_url")


@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("id", "cafe", "drink", "cost")


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ("cafe", "name", "lan", "lon")


@admin.register(Additional)
class Additional(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(ScheduleInCafe)
class ScheduleInCafeAdmin(admin.ModelAdmin):
    list_display = ("id", "cafe")


@admin.register(DrinkInCafe)
class DrinkInCafeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug",)

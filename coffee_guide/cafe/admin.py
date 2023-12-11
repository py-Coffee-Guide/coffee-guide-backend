from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from django.utils.html import format_html


from .models import (
    Cafe,
    City,
    Contact,
    District,
    Point,
    Schedule,
    StopFactor,
    ImageCafe
)


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    """Админка: Заведение"""

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = (
        "id",
        "name",
        "rating",
        "address"
    )
    list_filter = (
        "name",
        "rating",
        "address",
        "stop_factors"
    )

    fieldsets = (
        ("Основная информация",
            {"fields": (
                "name",
                "description",
                "rating",
                "stop_factors",
                # "poster"
            )}),
        (
            "Контакты и адреса",
            {"fields": (
                "address",
                "contact",
                "cities",
                "point")},
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


@admin.register(ImageCafe)
class ImageCafeAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "image_file",
        "image_url"
    )
    readonly_fields = ("image_tag",)

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" width="100" height="100" />'.format
            (obj.image_file.url)
        )

    image_tag.short_description = "Картинка"
    image_tag.allow_tags = True


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Админка: Город"""

    list_display = (
        "id",
        "name"
    )
    list_filter = ("name",)


@admin.register(StopFactor)
class StopFactorAdmin(admin.ModelAdmin):
    """Админка: Атрибуты"""

    list_display = (
        "id",
        "name",
        "slug"
    )
    list_filter = ("name",)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Админка: Время работы"""

    list_display = (
        "cafe",
        "day",
        "day_off",
        "start",
        "end"
    )
    # list_filter = (
    #     "cafe",
    #     "day",
    #     "day_off",
    #     "start",
    #     "end"
    # )


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    """Админка: Район"""

    list_display = ("name",)
    list_filter = ("name",)


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    """Админка: Координаты"""

    list_display = (
        "lat",
        "lon"
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админка: Контакты"""

    list_display = (
        "id",
        "phone",
        "website",
        "email"
        )
    list_filter = ("website",)

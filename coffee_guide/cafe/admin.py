from django.contrib import admin

# from django.utils.safestring import mark_safe

from .models import (
    Cafe,
    City,
    Contact,
    District,
    Point,
    Schedule,
    StopFactor,
)


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in Cafe._meta.get_fields()]

    # list_display = (
    #     "name",
    #     "id",
    #     "email",
    #     "is_verified",
    # )
    # fieldsets = (
    #     ("Основная информация", {"fields": ("owner", "name", "poster")}),
    #     (
    #         "Контакты и адреса",
    #         {"fields": ("cities", "address", "telephone", "email")},
    #     ),
    # )
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
    #
    # preview.short_description = "Превью"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in City._meta.get_fields()]


@admin.register(StopFactor)
class StopFactorAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in StopFactor._meta.get_fields()]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in Schedule._meta.get_fields()]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in District._meta.get_fields()]


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in Point._meta.get_fields()]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = [field.name for field in Contact._meta.get_fields()]

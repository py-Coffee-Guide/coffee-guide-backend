from django.contrib import admin

from .models import (
    Cafe,
    City,
    Contact,
    District,
    Metro,
    Point,
    Schedule,
    StopFactor,
)

# from django.utils.safestring import mark_safe


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    """Админка: Заведение"""

    # list_display = [field.name for field in Cafe._meta.get_fields()]
    list_display = [field.name for field in Cafe._meta.fields]
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
    """Админка: Город"""

    list_display = [field.name for field in City._meta.fields]


@admin.register(StopFactor)
class StopFactorAdmin(admin.ModelAdmin):
    """Админка: Атрибуты"""

    list_display = [field.name for field in StopFactor._meta.get_fields()]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Админка: Время работы"""

    list_display = [field.name for field in Schedule._meta.get_fields()]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    """Админка: Район"""

    list_display = [field.name for field in District._meta.get_fields()]


@admin.register(Metro)
class MetroAdmin(admin.ModelAdmin):
    """Админка: Метро"""

    list_display = [field.name for field in Metro._meta.fields]


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    """Админка: Координаты"""

    list_display = [field.name for field in Point._meta.get_fields()]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Админка: Контакты"""

    list_display = [field.name for field in Contact._meta.get_fields()]

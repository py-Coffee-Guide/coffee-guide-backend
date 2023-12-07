from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import (
    Establishment,
)


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    """Админка: заведение"""

    list_display = (
        "name",
        "id",
        "email",
        "is_verified",
    )
    fieldsets = (
        ("Основная информация", {"fields": ("owner", "name", "poster")}),
        (
            "Контакты и адреса",
            {"fields": ("cities", "address", "telephone", "email")},
        ),
    )
    list_filter = ("name",)
    empty_value_display = "-пусто-"
    autocomplete_fields = ["cities"]

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

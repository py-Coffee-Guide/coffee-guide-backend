from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "phone",
    )
    search_fields = (
        "username",
        "phone",
    )
    list_filter = (
        "username",
        "phone",
    )
    empty_value_display = "-пусто-"

from django.contrib import admin

from ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Админка: рейтинг"""
    model = Rating
    search_fields = ("text",)
    list_filter = ("establishment",)
    list_display = ("id", "establishment")

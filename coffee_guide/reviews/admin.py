from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка: отзывы"""
    model = Review
    search_fields = ("text",)
    list_filter = ("establishment", "created")
    list_display = ("id", "author", "establishment")

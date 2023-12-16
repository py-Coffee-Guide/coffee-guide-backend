from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка: отзывы"""

    list_display = ("id", "cafe", "author", "score", "pub_date")
    search_fields = ("cafe__name", "author__username")
    list_filter = ("score", "pub_date")
    readonly_fields = ("pub_date",)

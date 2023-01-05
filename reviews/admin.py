from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class BadFilter(admin.SimpleListFilter):

    title = "Filtering Bad Review!"

    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "3점 이상"),
            ("bad", "3점 이하"),
        ]

    def queryset(self, request, reviews):
        rating = self.value()
        # rating = request.GET.get("rating") 이걸로도 대체 가능
        if rating == "good":
            return reviews.filter(rating__gte=3)
        elif rating == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        BadFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )

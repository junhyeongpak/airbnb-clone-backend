from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250, default="")
    start_at = models.TimeField()
    end_at = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    category = models.ForeignKey(
        "categories.Category",
        # null = True와 blank = True를 하는 이유
        # -> SET_NULL의 설정을 위해서
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """What is included on an Experiences"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name

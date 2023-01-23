from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    file = models.URLField()  # 파일을 서버에 놓는 것이 아니라 클라우드 환경에 둘 것임
    description = models.CharField(
        max_length=140,
    )
    # photo가 room을 가리키는 것임
    # room은 가리킴 받는 것
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    file = models.URLField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "Video File"

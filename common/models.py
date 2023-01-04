from django.db import models

# Abstract 모델(추상화 클래스)를 만들 것임
# 이 클래스는 직접적으로 DB에 추가하지 않을 model이다. -> 재사용을 위한 모델


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

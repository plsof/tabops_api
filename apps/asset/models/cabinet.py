from django.db import models

from common.models import BaseModel
from .idc import Idc


class Cabinet(BaseModel):
    idc = models.ForeignKey(Idc, on_delete=models.CASCADE, verbose_name='机房')
    name = models.CharField(max_length=30, unique=True, verbose_name="机柜编号")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机柜"
        verbose_name_plural = verbose_name

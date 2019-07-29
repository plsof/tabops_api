from django.db import models

from common.models import BaseModel
from .idc import Idc
from .cabinet import Cabinet


class Rack(BaseModel):
    idc = models.ForeignKey(Idc, verbose_name='IDC', on_delete=models.CASCADE, blank=True, null=True)
    cabinet = models.ForeignKey(Cabinet, verbose_name='Cabinet', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30, verbose_name="机架编号")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机架"
        verbose_name_plural = verbose_name

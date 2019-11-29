from django.db import models

from common.models import BaseModel
from common.constants import ISP


class Idc(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='机房名称')
    address = models.CharField(max_length=255, verbose_name='机房地址')
    isp = models.IntegerField(verbose_name='运营商', default=0, choices=ISP)
    bandwidth = models.CharField(max_length=255, blank=True, null=True, verbose_name='带宽')
    # cabinet_num = models.IntegerField(blank=True, null=True, verbose_name='机柜数量')
    ip_range = models.TextField(blank=True, null=True, verbose_name="IP地址段")
    comment = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机房"
        verbose_name_plural = verbose_name

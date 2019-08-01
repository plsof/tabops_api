from django.db import models

from common.models import BaseModel
from .idc import Idc
from .cabinet import Cabinet
from .rack import Rack


class SHost(BaseModel):
    idc = models.ForeignKey(Idc, on_delete=models.CASCADE, verbose_name='机房')
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, blank=True, null=True, verbose_name='机柜')
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, blank=True, null=True, verbose_name='机架')
    hostname = models.CharField(max_length=255, blank=True, null=True, verbose_name="主机名")
    lan_ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="内网IP地址")
    man_ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="管理IP地址")
    serial_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="SN号")
    os = models.CharField(max_length=255, blank=True, null=True, verbose_name="操作系统")
    mem_total = models.IntegerField(blank=True, null=True, verbose_name="内存大小")
    num_cpus = models.IntegerField(blank=True, null=True, verbose_name="CPU数量")
    volume = models.CharField(max_length=255, blank=True, null=True, verbose_name="磁盘容量")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "宿主机"
        verbose_name_plural = verbose_name

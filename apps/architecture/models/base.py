from django.db import models

from common.constants import Z_STATUS
from common.models import BaseModel
from asset.models import Idc
from bstype.models import Bussiness, Service


class Base(BaseModel):
    idc = models.ForeignKey(Idc, on_delete=models.CASCADE, blank=True, null=True, verbose_name='机房')
    # bussiness = models.ForeignKey(Bussiness, on_delete=models.CASCADE, verbose_name='业务名称', blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True, verbose_name="服务名称")
    ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True, verbose_name="IP地址")
    path = models.CharField(max_length=255, blank=True, null=True, verbose_name='部署路径')
    port = models.IntegerField(blank=True, null=True, verbose_name="端口号")
    status = models.IntegerField(blank=True, null=True, verbose_name='zabbix状态', default=2, choices=Z_STATUS)
    comment = models.TextField(max_length=255, blank=True, null=True, verbose_name="备注")

    # def __str__(self):
    #     return self.service

    class Meta:
        abstract = True

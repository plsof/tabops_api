from django.db import models

from common.models import BaseModel
from common.constants import MINION_STATUS, Z_STATUS

# from .idc import Idc
# from .cabinet import Cabinet
# from .rack import Rack
# from .shost import SHost


class Host(BaseModel):
    idc = models.CharField(max_length=255, blank=True, null=True, verbose_name='机房')
    # cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, blank=True, null=True, verbose_name="机柜")
    # rack = models.ForeignKey(Rack, on_delete=models.CASCADE, blank=True, null=True, verbose_name="机架")
    # s_host = models.ForeignKey(SHost, on_delete=models.CASCADE, blank=True, null=True, verbose_name='宿主机')
    salt_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="SaltID")
    lan_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="内网IP地址")  # 不能设置为unique 会有重复lan_ip(salt-minion配置错误)
    man_ip = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name="管理IP地址")
    kernel = models.CharField(max_length=255, blank=True, null=True, verbose_name="系统内核")
    kernel_release = models.CharField(max_length=255, blank=True, null=True, verbose_name="系统内核版本")
    platform = models.CharField(max_length=255, blank=True, null=True, verbose_name="设备类型")
    hostname = models.CharField(max_length=255, blank=True, null=True, verbose_name="主机名")
    os_release = models.CharField(max_length=255, blank=True, null=True, verbose_name="操作系统版本")
    salt_version = models.CharField(max_length=255, blank=True, null=True, verbose_name="Salt版本")
    os_finger = models.CharField(max_length=255, blank=True, null=True, verbose_name="系统指纹")
    os_family = models.CharField(max_length=255, blank=True, null=True, verbose_name="系统类型")
    serial_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="SN号")
    cpu_model = models.CharField(max_length=255, blank=True, null=True, verbose_name="CPU型号")
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="产品名称")
    os_arch = models.CharField(max_length=255, blank=True, null=True, verbose_name="系统架构")
    cpu_arch = models.CharField(max_length=255, blank=True, null=True, verbose_name="CPU架构")
    os = models.CharField(max_length=255, blank=True, null=True, verbose_name="操作系统")
    mem_total = models.IntegerField(blank=True, null=True, verbose_name="内存大小")
    num_cpus = models.IntegerField(blank=True, null=True, verbose_name="CPU数量")
    z_status = models.IntegerField(verbose_name='Zabbix状态', default=2, choices=Z_STATUS)
    m_status = models.IntegerField(verbose_name='Minion状态', default=2, choices=MINION_STATUS)
    roles = models.CharField(max_length=255, blank=True, null=True, verbose_name="服务角色")
    comment = models.TextField(max_length=255, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return self.lan_ip

    class Meta:
        ordering = ['idc', 'lan_ip']
        verbose_name = "主机"
        verbose_name_plural = verbose_name

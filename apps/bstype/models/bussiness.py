from django.db import models

from common.models import BaseModel
from common.constants import B_TYPE


class Bussiness(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='业务名称')
    btype = models.IntegerField(verbose_name='业务类型', default=0, choices=B_TYPE)
    domain = models.CharField(max_length=255, blank=True, null=True, verbose_name='域名')
    comment = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '业务类型'
        verbose_name_plural = verbose_name

from django.db import models

from common.models import BaseModel
from .bussiness import Bussiness


class Service(BaseModel):
    bussiness = models.ForeignKey(Bussiness, related_name='bussiness_name', on_delete=models.CASCADE, verbose_name='业务类型')
    name = models.CharField(max_length=255, unique=True, verbose_name='服务类型')
    comment = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['bussiness', 'name']
        verbose_name = '服务类型'
        verbose_name_plural = verbose_name

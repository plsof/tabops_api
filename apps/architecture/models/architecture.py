from .base import Base


class Wtv(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '电视看点'
        verbose_name_plural = verbose_name

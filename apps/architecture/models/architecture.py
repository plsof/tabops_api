from .base import Base


class Wtv(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '电视看点'
        verbose_name_plural = verbose_name


class BImsBoot(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '终端管理'
        verbose_name_plural = verbose_name


class BImsPanel(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '桌面管理'
        verbose_name_plural = verbose_name


class Tms(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '播控认证'
        verbose_name_plural = verbose_name


class Epg(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '播控点播'
        verbose_name_plural = verbose_name


class Search(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '融合搜索'
        verbose_name_plural = verbose_name


class Pic(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '图片'
        verbose_name_plural = verbose_name


class Ppl(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '看单'
        verbose_name_plural = verbose_name


class CosEpg(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '融合EPG'
        verbose_name_plural = verbose_name


class Uic(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '用户中心'
        verbose_name_plural = verbose_name


class MScreen(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '多屏'
        verbose_name_plural = verbose_name


class DMS2(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'DMS2.0'
        verbose_name_plural = verbose_name


class XMpp(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = '消息系统'
        verbose_name_plural = verbose_name


class NDms(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'NDMS'
        verbose_name_plural = verbose_name


class TOS(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'TOS'
        verbose_name_plural = verbose_name


class UCS(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'UCS'
        verbose_name_plural = verbose_name


class MGS(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'MGS'
        verbose_name_plural = verbose_name


class NMC(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'NMC'
        verbose_name_plural = verbose_name


class UBS(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'UBS'
        verbose_name_plural = verbose_name


class VAS(Base):

    class Meta:
        ordering = ['idc', 'service', 'ip']
        verbose_name = 'VAS'
        verbose_name_plural = verbose_name

from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

    class Meta:
        ordering = ['file']
        verbose_name = '文件上传'
        verbose_name_plural = verbose_name

from .base import BaseSerializer
from architecture import models


class WtvSerializer(BaseSerializer):

    class Meta:
        model = models.Wtv
        fields = '__all__'


class BImsBootSerializer(BaseSerializer):

    class Meta:
        model = models.BImsBoot
        fields = '__all__'


class BImsPanelSerializer(BaseSerializer):

    class Meta:
        model = models.BImsPanel
        fields = '__all__'


class TmsSerializer(BaseSerializer):

    class Meta:
        model = models.Tms
        fields = '__all__'


class EpgSerializer(BaseSerializer):

    class Meta:
        model = models.Epg
        fields = '__all__'


class SearchSerializer(BaseSerializer):

    class Meta:
        model = models.Search
        fields = '__all__'


class PicSerializer(BaseSerializer):

    class Meta:
        model = models.Pic
        fields = '__all__'


class PplSerializer(BaseSerializer):

    class Meta:
        model = models.Ppl
        fields = '__all__'


class CosEpgSerializer(BaseSerializer):

    class Meta:
        model = models.CosEpg
        fields = '__all__'


class UicSerializer(BaseSerializer):

    class Meta:
        model = models.Uic
        fields = '__all__'


class MScreenSerializer(BaseSerializer):

    class Meta:
        model = models.MScreen
        fields = '__all__'


class DMS2Serializer(BaseSerializer):

    class Meta:
        model = models.DMS2
        fields = '__all__'


class XMppSerializer(BaseSerializer):

    class Meta:
        model = models.XMpp
        fields = '__all__'


class NDmsSerializer(BaseSerializer):

    class Meta:
        model = models.NDms
        fields = '__all__'


class TOSSerializer(BaseSerializer):

    class Meta:
        model = models.TOS
        fields = '__all__'


class UCSSerializer(BaseSerializer):

    class Meta:
        model = models.UCS
        fields = '__all__'


class MGSSerializer(BaseSerializer):

    class Meta:
        model = models.MGS
        fields = '__all__'


class NMCSerializer(BaseSerializer):

    class Meta:
        model = models.NMC
        fields = '__all__'


class UBSSerializer(BaseSerializer):

    class Meta:
        model = models.UBS
        fields = '__all__'


class VASSerializer(BaseSerializer):

    class Meta:
        model = models.VAS
        fields = '__all__'

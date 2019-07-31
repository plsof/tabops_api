from .base import BaseSerializer

from ..models import Wtv
from ..models import BImsBoot
from ..models import BImsPanel
from ..models import Tms
from ..models import Epg
from ..models import Search
from ..models import Pic
from ..models import Ppl
from ..models import CosEpg
from ..models import Uic
from ..models import MScreen
from ..models import DMS2
from ..models import XMpp
from ..models import NDms


class WtvSerializer(BaseSerializer):

    class Meta:
        model = Wtv
        fields = '__all__'


class BImsBootSerializer(BaseSerializer):

    class Meta:
        model = BImsBoot
        fields = '__all__'


class BImsPanelSerializer(BaseSerializer):

    class Meta:
        model = BImsPanel
        fields = '__all__'


class TmsSerializer(BaseSerializer):

    class Meta:
        model = Tms
        fields = '__all__'


class EpgSerializer(BaseSerializer):

    class Meta:
        model = Epg
        fields = '__all__'


class SearchSerializer(BaseSerializer):

    class Meta:
        model = Search
        fields = '__all__'


class PicSerializer(BaseSerializer):

    class Meta:
        model = Pic
        fields = '__all__'


class PplSerializer(BaseSerializer):

    class Meta:
        model = Ppl
        fields = '__all__'


class CosEpgSerializer(BaseSerializer):

    class Meta:
        model = CosEpg
        fields = '__all__'


class UicSerializer(BaseSerializer):

    class Meta:
        model = Uic
        fields = '__all__'


class MScreenSerializer(BaseSerializer):

    class Meta:
        model = MScreen
        fields = '__all__'


class DMS2Serializer(BaseSerializer):

    class Meta:
        model = DMS2
        fields = '__all__'


class XMppSerializer(BaseSerializer):

    class Meta:
        model = XMpp
        fields = '__all__'


class NDmsSerializer(BaseSerializer):

    class Meta:
        model = NDms
        fields = '__all__'

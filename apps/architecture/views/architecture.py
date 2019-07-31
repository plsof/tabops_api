from common.serializer import ResponseModelViewSet

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

from ..serializer import WtvSerializer
from ..serializer import BImsBootSerializer
from ..serializer import BImsPanelSerializer
from ..serializer import TmsSerializer
from ..serializer import EpgSerializer
from ..serializer import SearchSerializer
from ..serializer import PicSerializer
from ..serializer import PplSerializer
from ..serializer import CosEpgSerializer
from ..serializer import UicSerializer
from ..serializer import MScreenSerializer
from ..serializer import DMS2Serializer
from ..serializer import XMppSerializer
from ..serializer import NDmsSerializer


class WtvViewSet(ResponseModelViewSet):
    serializer_class = WtvSerializer
    model = Wtv

    def get_queryset(self):
        queryset = Wtv.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class BImsBootViewSet(ResponseModelViewSet):
    serializer_class = BImsBootSerializer
    model = BImsBoot

    def get_queryset(self):
        queryset = BImsBoot.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class BImsPanelViewSet(ResponseModelViewSet):
    serializer_class = BImsPanelSerializer
    model = BImsPanel

    def get_queryset(self):
        queryset = BImsPanel.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class TmsViewSet(ResponseModelViewSet):
    serializer_class = TmsSerializer
    model = Tms

    def get_queryset(self):
        queryset = Tms.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class EpgViewSet(ResponseModelViewSet):
    serializer_class = EpgSerializer
    model = Epg

    def get_queryset(self):
        queryset = Epg.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class SearchViewSet(ResponseModelViewSet):
    serializer_class = SearchSerializer
    model = Search

    def get_queryset(self):
        queryset = Search.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class PicViewSet(ResponseModelViewSet):
    serializer_class = PicSerializer
    model = Pic

    def get_queryset(self):
        queryset = Pic.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class PplViewSet(ResponseModelViewSet):
    serializer_class = PplSerializer
    model = Ppl

    def get_queryset(self):
        queryset = Ppl.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class CosEpgViewSet(ResponseModelViewSet):
    serializer_class = CosEpgSerializer
    model = CosEpg

    def get_queryset(self):
        queryset = CosEpg.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class UicViewSet(ResponseModelViewSet):
    serializer_class = UicSerializer
    model = Uic

    def get_queryset(self):
        queryset = Uic.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class MScreenViewSet(ResponseModelViewSet):
    serializer_class = MScreenSerializer
    model = MScreen

    def get_queryset(self):
        queryset = MScreen.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class DMS2ViewSet(ResponseModelViewSet):
    serializer_class = DMS2Serializer
    model = DMS2

    def get_queryset(self):
        queryset = DMS2.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class XMppViewSet(ResponseModelViewSet):
    serializer_class = XMppSerializer
    model = XMpp

    def get_queryset(self):
        queryset = XMpp.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class NDmsViewSet(ResponseModelViewSet):
    serializer_class = NDmsSerializer
    model = NDms

    def get_queryset(self):
        queryset = NDms.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset

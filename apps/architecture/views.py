from common.views import ResponseModelViewSet
from architecture import models
from architecture import serializer


class WtvViewSet(ResponseModelViewSet):
    serializer_class = serializer.WtvSerializer

    def get_queryset(self):
        queryset = models.Wtv.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class BImsBootViewSet(ResponseModelViewSet):
    serializer_class = serializer.BImsBootSerializer

    def get_queryset(self):
        queryset = models.BImsBoot.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class BImsPanelViewSet(ResponseModelViewSet):
    serializer_class = serializer.BImsPanelSerializer

    def get_queryset(self):
        queryset = models.BImsPanel.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class TmsViewSet(ResponseModelViewSet):
    serializer_class = serializer.TmsSerializer

    def get_queryset(self):
        queryset = models.Tms.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class EpgViewSet(ResponseModelViewSet):
    serializer_class = serializer.EpgSerializer

    def get_queryset(self):
        queryset = models.Epg.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class SearchViewSet(ResponseModelViewSet):
    serializer_class = serializer.SearchSerializer

    def get_queryset(self):
        queryset = models.Search.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class PicViewSet(ResponseModelViewSet):
    serializer_class = serializer.PicSerializer

    def get_queryset(self):
        queryset = models.Pic.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class PplViewSet(ResponseModelViewSet):
    serializer_class = serializer.PplSerializer

    def get_queryset(self):
        queryset = models.Ppl.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class CosEpgViewSet(ResponseModelViewSet):
    serializer_class = serializer.CosEpgSerializer

    def get_queryset(self):
        queryset = models.CosEpg.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class UicViewSet(ResponseModelViewSet):
    serializer_class = serializer.UicSerializer

    def get_queryset(self):
        queryset = models.Uic.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class MScreenViewSet(ResponseModelViewSet):
    serializer_class = serializer.MScreenSerializer

    def get_queryset(self):
        queryset = models.MScreen.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class DMS2ViewSet(ResponseModelViewSet):
    serializer_class = serializer.DMS2Serializer

    def get_queryset(self):
        queryset = models.DMS2.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class XMppViewSet(ResponseModelViewSet):
    serializer_class = serializer.XMppSerializer

    def get_queryset(self):
        queryset = models.XMpp.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class NDmsViewSet(ResponseModelViewSet):
    serializer_class = serializer.NDmsSerializer

    def get_queryset(self):
        queryset = models.NDms.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class TOSViewSet(ResponseModelViewSet):
    serializer_class = serializer.TOSSerializer

    def get_queryset(self):
        queryset = models.TOS.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class UCSViewSet(ResponseModelViewSet):
    serializer_class = serializer.UCSSerializer

    def get_queryset(self):
        queryset = models.UCS.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class MGSViewSet(ResponseModelViewSet):
    serializer_class = serializer.MGSSerializer

    def get_queryset(self):
        queryset = models.MGS.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class NMCViewSet(ResponseModelViewSet):
    serializer_class = serializer.NMCSerializer

    def get_queryset(self):
        queryset = models.NMC.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset


class UBSViewSet(ResponseModelViewSet):
    serializer_class = serializer.UBSSerializer

    def get_queryset(self):
        queryset = models.UBS.objects.all()
        idc = self.request.query_params.get('idc', None)
        service = self.request.query_params.get('service', None)
        ip = self.request.query_params.get('ip', '').strip()
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        if ip is not None and ip is not '':
            queryset = queryset.filter(ip__contains=ip)
        return queryset

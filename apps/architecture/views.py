from common.views import ResponseModelViewSet
from architecture import models
from architecture import serializer


class ArchitectureViewSet(ResponseModelViewSet):

    def get_queryset(self):
        queryset = self.queryset
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


class WtvViewSet(ArchitectureViewSet):

    serializer_class = serializer.WtvSerializer
    queryset = models.Wtv.objects.all()


class BImsBootViewSet(ArchitectureViewSet):

    serializer_class = serializer.BImsBootSerializer
    queryset = models.BImsBoot.objects.all()


class BImsPanelViewSet(ArchitectureViewSet):

    serializer_class = serializer.BImsPanelSerializer
    queryset = models.BImsPanel.objects.all()


class TmsViewSet(ArchitectureViewSet):

    serializer_class = serializer.TmsSerializer
    queryset = models.Tms.objects.all()


class EpgViewSet(ArchitectureViewSet):

    serializer_class = serializer.EpgSerializer
    queryset = models.Epg.objects.all()


class SearchViewSet(ArchitectureViewSet):

    serializer_class = serializer.SearchSerializer
    queryset = models.Search.objects.all()


class PicViewSet(ArchitectureViewSet):

    serializer_class = serializer.PicSerializer
    queryset = models.Pic.objects.all()


class PplViewSet(ArchitectureViewSet):

    serializer_class = serializer.PplSerializer
    queryset = models.Ppl.objects.all()


class CosEpgViewSet(ArchitectureViewSet):

    serializer_class = serializer.CosEpgSerializer
    queryset = models.CosEpg.objects.all()


class UicViewSet(ArchitectureViewSet):

    serializer_class = serializer.UicSerializer
    queryset = models.Uic.objects.all()


class MScreenViewSet(ArchitectureViewSet):

    serializer_class = serializer.MScreenSerializer
    queryset = models.MScreen.objects.all()


class DMS2ViewSet(ArchitectureViewSet):

    serializer_class = serializer.DMS2Serializer
    queryset = models.DMS2.objects.all()


class XMppViewSet(ArchitectureViewSet):

    serializer_class = serializer.XMppSerializer
    queryset = models.XMpp.objects.all()


class NDmsViewSet(ArchitectureViewSet):

    serializer_class = serializer.NDmsSerializer
    queryset = models.NDms.objects.all()


class TOSViewSet(ArchitectureViewSet):

    serializer_class = serializer.TOSSerializer
    queryset = models.TOS.objects.all()


class UCSViewSet(ArchitectureViewSet):

    serializer_class = serializer.UCSSerializer
    queryset = models.UCS.objects.all()


class MGSViewSet(ArchitectureViewSet):

    serializer_class = serializer.MGSSerializer
    queryset = models.MGS.objects.all()


class NMCViewSet(ArchitectureViewSet):

    serializer_class = serializer.NMCSerializer
    queryset = models.NMC.objects.all()


class UBSViewSet(ArchitectureViewSet):

    serializer_class = serializer.UBSSerializer
    queryset = models.UBS.objects.all()


class VASViewSet(ArchitectureViewSet):

    serializer_class = serializer.VASSerializer
    queryset = models.VAS.objects.all()


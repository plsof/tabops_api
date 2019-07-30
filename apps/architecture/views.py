from common.serializer import ResponseModelViewSet

from .models import Wtv
from .serializer import WtvSerializer


class WtvViewsets(ResponseModelViewSet):
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

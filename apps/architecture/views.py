from common.serializer import ResponseModelViewSet

from .models import Wtv
from .serializer import WtvSerializer


class WtvViewsets(ResponseModelViewSet):
    serializer_class = WtvSerializer
    model = Wtv

    def get_queryset(self):
        queryset = Wtv.objects.all()
        idc = self.request.query_params.get('idc', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        service = self.request.query_params.get('service', None)
        if service is not None and service is not '':
            queryset = queryset.filter(service=service)
        return queryset

from common.serializer import ResponseModelViewSet

from .models import Idc
from .serializer import IdcSerializer


class IdcViewsets(ResponseModelViewSet):
    serializer_class = IdcSerializer
    model = Idc

    def get_queryset(self):
        queryset = Idc.objects.all()
        isp = self.request.query_params.get('isp', None)
        if isp is not None and isp is not '':
            queryset = queryset.filter(isp=isp)
        return queryset

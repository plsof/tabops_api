from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from common.serializer import ResponseModelViewSet

from .models import Idc
from .models import Host
from .serializer import IdcSerializer
from .serializer import HostSerializer


# 获取全部数据，不分页
class IdcList(ListAPIView):

    def list(self, request):
        queryset = Idc.objects.all()
        response = {
            'code': 0,
            'data': [],
            'msg': 'success'
        }
        serializer = IdcSerializer(queryset, many=True)
        response['data'] = serializer.data
        return Response(response)


class IdcViewsets(ResponseModelViewSet):
    serializer_class = IdcSerializer
    model = Idc

    def get_queryset(self):
        queryset = Idc.objects.all()
        isp = self.request.query_params.get('isp', None)
        if isp is not None and isp is not '':
            queryset = queryset.filter(isp=isp)
        return queryset


class HostViewsets(ResponseModelViewSet):
    serializer_class = HostSerializer
    model = Host

    def get_queryset(self):
        queryset = Host.objects.all()
        idc = self.request.query_params.get('idc', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        return queryset

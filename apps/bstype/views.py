from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from common.views import ResponseModelViewSet
from bstype.models import Bussiness, Service
from .serializer import BussinessSerializer, ServiceSerializer


# 获取全部数据，不分页
class BussinessList(ListAPIView):

    def list(self, request):
        queryset = Bussiness.objects.all()
        response = {
            'code': 0,
            'data': [],
            'msg': 'success'
        }
        serializer = BussinessSerializer(queryset, many=True)
        response['data'] = serializer.data
        return Response(response)


class BussinessViewSet(ResponseModelViewSet):
    serializer_class = BussinessSerializer
    model = Bussiness

    def get_queryset(self):
        queryset = Bussiness.objects.all()
        btype = self.request.query_params.get('btype', None)
        if btype is not None and btype is not '':
            queryset = queryset.filter(btype=btype)
        return queryset


# 获取全部数据，不分页
class ServiceList(ListAPIView):

    def list(self, request):
        response = {
            'code': 0,
            'data': [],
            'msg': 'success'
        }
        queryset = Service.objects.all()
        bussiness = request.query_params.get('bussiness', None)
        if bussiness is not None and bussiness is not '':
            queryset = queryset.filter(bussiness=bussiness)
        serializer = ServiceSerializer(queryset, many=True)
        response['data'] = serializer.data
        return Response(response)


class ServiceViewSet(ResponseModelViewSet):
    serializer_class = ServiceSerializer
    model = Service

    def get_queryset(self):
        queryset = Service.objects.all()
        bussiness = self.request.query_params.get('bussiness', None)
        if bussiness is not None and bussiness is not '':
            queryset = queryset.filter(bussiness=bussiness)
        return queryset

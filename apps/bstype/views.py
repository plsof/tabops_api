from common.views import ResponseModelViewSet
from bstype import models
from bstype import serializer


class BussinessViewSet(ResponseModelViewSet):

    serializer_class = serializer.BussinessSerializer
    queryset = models.Bussiness.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        btype = self.request.query_params.get('btype', None)
        if btype is not None and btype is not '':
            queryset = queryset.filter(btype=btype)
        return queryset


class ServiceViewSet(ResponseModelViewSet):

    serializer_class = serializer.ServiceSerializer
    queryset = models.Service.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        bussiness = self.request.query_params.get('bussiness', None)
        if bussiness is not None and bussiness is not '':
            queryset = queryset.filter(bussiness=bussiness)
        return queryset

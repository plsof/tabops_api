from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from common.serializer import ResponseModelViewSet
from bstype.models import Bussiness, Service
from .serializer import BussinessSerializer, ServiceSerializer


class BussinessList(ListAPIView):

    def list(self, request):
        queryset = Bussiness.objects.all()
        serializer = BussinessSerializer(queryset, many=True)
        return Response({'data': serializer.data})


class BussinessViewsets(ResponseModelViewSet):
    serializer_class = BussinessSerializer
    model = Bussiness

    def get_queryset(self):
        queryset = Bussiness.objects.all()
        btype = self.request.query_params.get('btype', None)
        if btype is not None and btype is not '':
            queryset = queryset.filter(btype=btype)
        return queryset


class ServiceViewsets(ResponseModelViewSet):
    serializer_class = ServiceSerializer
    model = Service

    def get_queryset(self):
        queryset = Service.objects.all()
        bussiness = self.request.query_params.get('bussiness', None)
        if bussiness is not None and bussiness is not '':
            queryset = queryset.filter(bussiness=bussiness)
        return queryset

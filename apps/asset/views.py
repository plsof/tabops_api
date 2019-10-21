from common.views import ResponseModelViewSet
from .models import Idc
from .models import Host
from .serializer import IdcSerializer
from .serializer import HostSerializer


class IdcViewSet(ResponseModelViewSet):
    serializer_class = IdcSerializer

    def get_queryset(self):
        queryset = Idc.objects.all()
        isp = self.request.query_params.get('isp', None)
        if isp is not None and isp is not '':
            queryset = queryset.filter(isp=isp)
        return queryset


class HostViewSet(ResponseModelViewSet):
    serializer_class = HostSerializer

    def get_queryset(self):
        queryset = Host.objects.all()
        idc = self.request.query_params.get('idc', None)
        lan_ip = self.request.query_params.get('lan_ip', '').strip()
        roles = self.request.query_params.get('roles', '').strip()
        platform = self.request.query_params.get('platform', None)
        m_status = self.request.query_params.get('m_status', None)
        z_status = self.request.query_params.get('z_status', None)
        if idc is not None and idc is not '':
            queryset = queryset.filter(idc=idc)
        if lan_ip is not None and lan_ip is not '':
            queryset = queryset.filter(lan_ip__contains=lan_ip)
        if roles is not None and roles is not '':
            queryset = queryset.filter(roles__icontains=roles)
        if m_status is not None and m_status is not '':
            queryset = queryset.filter(m_status=m_status)
        if platform is not None and platform is not '':
            queryset = queryset.filter(platform=platform)
        if z_status is not None and z_status is not '':
            queryset = queryset.filter(z_status=z_status)
        return queryset

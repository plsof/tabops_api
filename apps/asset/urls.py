from django.urls import path, re_path

from .views import IdcList
from .views import IdcViewSet
from .views import HostViewSet

from .tasks import scan_host


urlpatterns = [
    path(r'idcall/', IdcList.as_view()),
    path(r'idc/', IdcViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^idc/(?P<pk>[0-9]+)$', IdcViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'host/', HostViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^host/(?P<pk>[0-9]+)$', HostViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    re_path(r'^scan/$', scan_host),
]

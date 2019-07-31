from django.urls import path, re_path

from .views import WtvViewSet
from .views import BImsBootViewSet
from .views import BImsPanelViewSet
from .views import TmsViewSet
from .views import EpgViewSet
from .views import SearchViewSet
from .views import PicViewSet
from .views import PplViewSet
from .views import CosEpgViewSet
from .views import UicViewSet
from .views import MScreenViewSet
from .views import DMS2ViewSet
from .views import XMppViewSet
from .views import NDmsViewSet

urlpatterns = [
    path(r'wtv/', WtvViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^wtv/(?P<pk>[0-9]+)$', WtvViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'bimsboot/', BImsBootViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^bimsboot/(?P<pk>[0-9]+)$', BImsBootViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'bimspanel/', BImsPanelViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^bimspanel/(?P<pk>[0-9]+)$', BImsPanelViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'tms/', TmsViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^tms/(?P<pk>[0-9]+)$', TmsViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'epg/', EpgViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^epg/(?P<pk>[0-9]+)$', EpgViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'epg/', EpgViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^epg/(?P<pk>[0-9]+)$', EpgViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'search/', SearchViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^search/(?P<pk>[0-9]+)$', SearchViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'pic/', PicViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^pic/(?P<pk>[0-9]+)$', PicViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'ppl/', PplViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^ppl/(?P<pk>[0-9]+)$', PplViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'cosepg/', CosEpgViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^cosepg/(?P<pk>[0-9]+)$', CosEpgViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'uic/', UicViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^uic/(?P<pk>[0-9]+)$', UicViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'mscreen/', MScreenViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^mscreen/(?P<pk>[0-9]+)$', MScreenViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'dms2/', DMS2ViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^dms2/(?P<pk>[0-9]+)$', DMS2ViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'xmpp/', XMppViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^xmpp/(?P<pk>[0-9]+)$', XMppViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'ndms/', NDmsViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^ndms/(?P<pk>[0-9]+)$', NDmsViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
]

from django.urls import path, re_path

from .views import IdcList
from .views import IdcViewsets


urlpatterns = [
    path(r'idcall/', IdcList.as_view()),
    path(r'idc/', IdcViewsets.as_view({"get": "list", "post": "create"})),
    re_path(r'^idc/(?P<pk>[0-9]+)$', IdcViewsets.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
]

from django.urls import path, re_path

from .views import BussinessViewSet, ServiceViewSet


urlpatterns = [
    path(r'bussiness/', BussinessViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^bussiness/(?P<pk>[0-9]+)$', BussinessViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
    path(r'service/', ServiceViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^service/(?P<pk>[0-9]+)$', ServiceViewSet.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
]

from django.urls import path, re_path

from .views import WtvViewsets


urlpatterns = [
    path(r'wtv/', WtvViewsets.as_view({"get": "list", "post": "create"})),
    re_path(r'^wtv/(?P<pk>[0-9]+)$', WtvViewsets.as_view({"put": "update", "patch": "partial_update", "delete": "destroy"})),
]

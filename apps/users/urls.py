from django.urls import path, re_path

from .views import UserViewSet

urlpatterns = [
    path(r'register/', UserViewSet.as_view({"post": "create"})),
    path(r'info/', UserViewSet.as_view({"get": "list"})),
    # re_path(r'^update/(?P<pk>[0-9]+)$', UserViewSet.as_view({"put": "update"})),
    re_path(r'^info/(?P<pk>[0-9]+)$', UserViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"})),
]

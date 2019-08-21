from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import UserViewSet

urlpatterns = [
    path(r'login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # re_path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    path(r'register/', UserViewSet.as_view({"post": "create"})),
    path(r'info/', UserViewSet.as_view({"get": "list"})),
    # re_path(r'^update/(?P<pk>[0-9]+)$', UserViewSet.as_view({"put": "update"})),
    re_path(r'^info/(?P<pk>[0-9]+)$', UserViewSet.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"})),
]

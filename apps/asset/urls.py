from django.urls import path, include
from rest_framework.routers import DefaultRouter

from asset import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'idc', views.IdcViewSet, basename='Idc')
router.register(r'host', views.HostViewSet, basename='Host')

urlpatterns = [
    path('', include(router.urls)),
]

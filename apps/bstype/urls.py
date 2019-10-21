from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bstype import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bussiness', views.BussinessViewSet, basename='Bussiness')
router.register(r'service', views.ServiceViewSet, basename='Service')

urlpatterns = [
    path('', include(router.urls)),
]


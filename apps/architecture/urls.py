from django.urls import path, include
from rest_framework.routers import DefaultRouter

from architecture import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'wtv', views.WtvViewSet, basename='Wtv')
router.register(r'bimsboot', views.BImsBootViewSet, basename='BImsBoot')
router.register(r'bimspanel', views.BImsPanelViewSet, basename='BImsPanel')
router.register(r'tms', views.TmsViewSet, basename='Tms')
router.register(r'epg', views.EpgViewSet, basename='Epg')
router.register(r'search', views.SearchViewSet, basename='Search')
router.register(r'pic', views.PicViewSet, basename='Pic')
router.register(r'ppl', views.PplViewSet, basename='Ppl')
router.register(r'cosepg', views.CosEpgViewSet, basename='CosEpg')
router.register(r'uic', views.UicViewSet, basename='Uic')
router.register(r'mscreen', views.MScreenViewSet, basename='MScreen')
router.register(r'dms2', views.DMS2ViewSet, basename='DMS2')
router.register(r'xmpp', views.XMppViewSet, basename='XMpp')
router.register(r'ndms', views.NDmsViewSet, basename='NDms')
router.register(r'tos', views.TOSViewSet, basename='TOS')
router.register(r'ucs', views.UCSViewSet, basename='UCS')
router.register(r'mgs', views.MGSViewSet, basename='MGS')
router.register(r'nmc', views.NMCViewSet, basename='NMC')
router.register(r'ubs', views.UBSViewSet, basename='UBS')

urlpatterns = [
    path('', include(router.urls)),
]

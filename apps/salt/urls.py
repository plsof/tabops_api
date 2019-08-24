from django.urls import path

from .scan import scan_minion

urlpatterns = [
    path(r'scan/', scan_minion),
]

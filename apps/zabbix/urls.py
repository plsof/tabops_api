from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from zabbix import refresh

urlpatterns = [
    path(r'refresh/port/', csrf_exempt(refresh.PortRefresh.as_view())),
    path(r'refresh/agent/', csrf_exempt(refresh.AgentRefresh.as_view()))
]

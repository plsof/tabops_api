from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from zabbix import views

urlpatterns = [
    path(r'refresh/port/', csrf_exempt(views.PortRefresh.as_view())),
    path(r'refresh/agent/', csrf_exempt(views.AgentRefresh.as_view()))
]

from django.urls import path

from .refresh import refresh_port
from .refresh import refresh_agent

urlpatterns = [
    path(r'refresh/port/', refresh_port),
    path(r'refresh/agent/', refresh_agent)
]

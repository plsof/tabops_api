from django.urls import path

from .refresh import refresh_port

urlpatterns = [
    path(r'refresh/', refresh_port),
]

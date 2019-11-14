from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from salt import views

urlpatterns = [
    path(r'scan/', csrf_exempt(views.ScanMinion.as_view())),
]

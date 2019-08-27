from __future__ import absolute_import
from celery import shared_task
import json
import logging
import requests
from django.db.models import Q

from architecture.models import Wtv
from architecture.models import BImsBoot
from architecture.models import BImsPanel
from architecture.models import Tms
from architecture.models import Epg
from architecture.models import Search
from architecture.models import Pic
from architecture.models import Ppl
from architecture.models import CosEpg
from architecture.models import Uic
from architecture.models import MScreen
from architecture.models import DMS2
from architecture.models import XMpp
from architecture.models import NDms
from .zabbix_token import zabbix_token
from tabops_api.settings import DEFAULT_LOGGER, ZABBIX_API_URL

logger = logging.getLogger(DEFAULT_LOGGER)


def zabbix_port(qs):
    token = zabbix_token()
    port = "net.tcp.service[tcp,,%s]" % qs.port
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "host": qs.ip,
            "search": {
                "key_": port
            }
        },
        "auth": token,
        "id": 1
    }
    try:
        ret = requests.post(ZABBIX_API_URL, data=json.dumps(payload), headers=headers, timeout=5, verify=False)
    except requests.ConnectionError as e:
        logging.error(e)
        return 1
    res = json.loads(ret.text)
    if res["result"]:
        status = res["result"][0]["lastvalue"]
    else:
        status = 2
    status = int(status)
    qs.status = status
    qs.save()


@shared_task
def refresh_port_wtv():
    queryset = Wtv.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_bimsboot():
    queryset = BImsBoot.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_bimspanel():
    queryset = BImsPanel.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_tms():
    queryset = Tms.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_epg():
    queryset = Epg.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_search():
    queryset = Search.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_pic():
    queryset = Pic.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_ppl():
    queryset = Ppl.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_cosepg():
    queryset = CosEpg.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_uic():
    queryset = Uic.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_mscreen():
    queryset = MScreen.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_dms2():
    queryset = DMS2.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_xmpp():
    queryset = XMpp.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)


@shared_task
def refresh_port_ndms():
    queryset = NDms.objects.filter(~Q(port=None))
    for qs in queryset:
        zabbix_port(qs)



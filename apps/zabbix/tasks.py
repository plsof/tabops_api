from __future__ import absolute_import
from celery import shared_task
import json
import logging
import requests
from django.db.models import Q

from zabbix.zabbix_api import token_get
from architecture import models
from tabops_api.settings import DEFAULT_LOGGER, ZABBIX_API_URL_WEST, ZABBIX_API_URL_SOUTH

logger = logging.getLogger(DEFAULT_LOGGER)

HEADERS = {'Content-Type': 'application/json'}

PAYLOAD = {
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "host": '',
        "search": {
            "key_": ''
        }
    },
    "auth": '',
    "id": 1
}


def zabbix_port(queryset):
    # south
    s_con = Q()
    qs1 = Q()
    qs1.connector = 'OR'
    qs1.children.append(('idc__name', '109'))
    qs1.children.append(('idc__name', '111'))
    qs1.children.append(('idc__name', '210'))
    qs2 = Q()
    qs2.connector = 'OR'
    qs2.children.append(~Q(port=3306))  # 排除mysql，用的net.tcp.listen[]
    s_con.add(qs1, 'AND')
    s_con.add(qs2, 'AND')
    s_queryset = queryset.filter(s_con)
    s_token = token_get("z_token_south", ZABBIX_API_URL_SOUTH)
    # west
    w_con = Q()
    qw1 = Q()
    qw1.connector = 'OR'
    qw1.children.append(('idc__name', '301'))
    qw1.children.append(('idc__name', '601'))
    qw2 = Q()
    qw2.connector = 'OR'
    qw2.children.append(~Q(port=3306))
    w_con.add(qw1, 'AND')
    w_con.add(qw2, 'AND')
    w_queryset = queryset.filter(w_con)
    w_token = token_get("z_token_west", ZABBIX_API_URL_WEST)

    # south refresh
    for qs in s_queryset:
        port = "net.tcp.service[tcp,,%s]" % qs.port
        PAYLOAD['params']['host'] = qs.ip
        PAYLOAD['params']['search']['key_'] = port
        PAYLOAD['auth'] = s_token
        try:
            ret = requests.post(ZABBIX_API_URL_SOUTH, data=json.dumps(PAYLOAD), headers=HEADERS, timeout=5,
                                verify=False)
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
    # db.objects.bulk_update(s_queryset, ['port'])

    # west refresh
    for qs in w_queryset:
        port = "net.tcp.service[tcp,,%s]" % qs.port
        PAYLOAD['params']['host'] = qs.ip
        PAYLOAD['params']['search']['key_'] = port
        PAYLOAD['auth'] = w_token
        try:
            ret = requests.post(ZABBIX_API_URL_WEST, data=json.dumps(PAYLOAD), headers=HEADERS, timeout=5,
                                verify=False)
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
    # db.objects.bulk_update(w_queryset, ['port'])


@shared_task
def refresh_port_wtv():
    queryset = models.Wtv.objects.filter(~Q(port=None))
    zabbix_port(queryset)


# @shared_task
# def refresh_port_bimsboot():
#     queryset = models.BImsBoot.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_bimspanel():
#     queryset = models.BImsPanel.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_tms():
#     queryset = models.Tms.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_epg():
#     queryset = models.Epg.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_search():
#     queryset = models.Search.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_pic():
#     queryset = models.Pic.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_ppl():
#     queryset = models.Ppl.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_cosepg():
#     queryset = models.CosEpg.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_uic():
#     queryset = models.Uic.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_mscreen():
#     queryset = models.MScreen.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_dms2():
#     queryset = models.DMS2.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_xmpp():
#     queryset = models.XMpp.objects.filter(~Q(port=None))
#     zabbix_port(queryset)
#
#
# @shared_task
# def refresh_port_ndms():
#     queryset = models.NDms.objects.filter(~Q(port=None))
#     zabbix_port(queryset)

import json
import requests
import logging
from django.http import JsonResponse
from django.views.generic.base import View

from asset.models import Host
from architecture import models
from zabbix.zabbix_api import token_get
from common.views import ResponseInfo
from tabops_api.settings import DEFAULT_LOGGER, ZABBIX_API_URL_SOUTH, ZABBIX_API_URL_WEST

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


class PortRefresh(View):
    """
    刷新端口监控
    """
    def __init__(self):
        self.response_format = ResponseInfo().response

    def post(self, request):
        body = json.loads(request.body)
        db = body['db']
        aid = body['id']
        if db == 'Wtv':
            queryset = models.Wtv.objects.filter(id=aid)
        elif db == 'BImsBoot':
            queryset = models.BImsBoot.objects.filter(id=aid)
        elif db == 'BImsPanel':
            queryset = models.BImsPanel.objects.filter(id=aid)
        elif db == 'Tms':
            queryset = models.Tms.objects.filter(id=aid)
        elif db == 'Epg':
            queryset = models.Epg.objects.filter(id=aid)
        elif db == 'Search':
            queryset = models.Search.objects.filter(id=aid)
        elif db == 'Pic':
            queryset = models.Pic.objects.filter(id=aid)
        elif db == 'Ppl':
            queryset = models.Ppl.objects.filter(id=aid)
        elif db == 'CosEpg':
            queryset = models.CosEpg.objects.filter(id=aid)
        elif db == 'Uic':
            queryset = models.Uic.objects.filter(id=aid)
        elif db == 'MScreen':
            queryset = models.MScreen.objects.filter(id=aid)
        elif db == 'DMS2':
            queryset = models.DMS2.objects.filter(id=aid)
        elif db == 'XMpp':
            queryset = models.XMpp.objects.filter(id=aid)
        elif db == 'NDms':
            queryset = models.NDms.objects.filter(id=aid)
        elif db == 'TOS':
            queryset = models.TOS.objects.filter(id=aid)
        elif db == 'UCS':
            queryset = models.UCS.objects.filter(id=aid)
        elif db == 'MGS':
            queryset = models.MGS.objects.filter(id=aid)
        elif db == 'NMC':
            queryset = models.NMC.objects.filter(id=aid)
        elif db == 'UBS':
            queryset = models.UBS.objects.filter(id=aid)
        elif db == 'VAS':
            queryset = models.VAS.objects.filter(id=aid)
        values = queryset.values('ip', 'port')[0]
        if "10.1" in values['ip'] or "10.3" in values['ip']:
            zabbix_api_url = ZABBIX_API_URL_WEST
            token = token_get("z_token_west", zabbix_api_url)
        if "10.25" in values['ip'] or "172.188" in values['ip']:
            zabbix_api_url = ZABBIX_API_URL_SOUTH
            token = token_get("z_token_south", zabbix_api_url)
        # 只验证有端口的实例
        if values['port']:
            if values['port'] in [3306, 3307]:
                port = "net.tcp.listen[%d]" % values['port']
            else:
                port = "net.tcp.service[tcp,,%d]" % values['port']
            PAYLOAD['params']['host'] = values['ip']
            PAYLOAD['params']['search']['key_'] = port
            PAYLOAD['auth'] = token
            try:
                ret = requests.post(zabbix_api_url, data=json.dumps(PAYLOAD), headers=HEADERS, timeout=5, verify=False)
            except requests.ConnectionError as e:
                logging.error(e)
                return 1
            res = json.loads(ret.text)
            if res["result"]:
                status = res["result"][0]["lastvalue"]
            else:
                status = 2
        else:
            status = 2
        status = int(status)
        queryset.update(status=status)
        if status == 0:
            z_status = 'Down'
        elif status == 1:
            z_status = 'Up'
        elif status == 2:
            z_status = 'None'
        self.response_format['data'] = {'z_status': z_status}
        return JsonResponse(self.response_format)


class AgentRefresh(View):
    """
    刷新agent监控
    """
    def __init__(self):
        self.response_format = ResponseInfo().response

    def post(self, request):
        body = json.loads(request.body)
        aid = body['id']
        queryset = Host.objects.filter(id=aid)
        values = queryset.values('lan_ip')[0]
        if "10.1" in values['lan_ip'] or "10.3" in values['lan_ip']:
            zabbix_api_url = ZABBIX_API_URL_WEST
            token = token_get("z_token_west", zabbix_api_url)
        if "10.25" in values['lan_ip'] or "172.188" in values['lan_ip']:
            zabbix_api_url = ZABBIX_API_URL_SOUTH
            token = token_get("z_token_south", zabbix_api_url)
        if values:
            PAYLOAD['params']['host'] = values['lan_ip']
            PAYLOAD['params']['search']['key_'] = "agent.ping"
            PAYLOAD['auth'] = token
            try:
                ret = requests.post(zabbix_api_url, data=json.dumps(PAYLOAD), headers=HEADERS, timeout=5, verify=False)
            except requests.ConnectionError as e:
                logging.error(e)
                return 1
            res = json.loads(ret.text)
            if res["result"]:
                z_status = res["result"][0]["lastvalue"]
            else:
                z_status = 2
        else:
            z_status = 2
        z_status = int(z_status)
        queryset.update(z_status=z_status)
        if z_status == 0:
            zabbix_status = 'Down'
        elif z_status == 1:
            zabbix_status = 'Up'
        elif z_status == 2:
            zabbix_status = 'None'
        self.response_format['data'] = {'zabbix_status': zabbix_status}
        return JsonResponse(self.response_format)

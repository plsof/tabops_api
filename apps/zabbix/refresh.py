import json
import requests
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from asset.models import Host
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


@csrf_exempt
def refresh_port(request):
    """
    刷新端口监控
    :return:
    """
    response = {
        'code': 0,
        'data': [],
        'msg': '刷新完成',
        'total': 0
    }
    if request.method == 'POST':
        body = json.loads(request.body)
        db = body['db']
        aid = body['id']
        if db == 'Wtv':
            queryset = Wtv.objects.filter(id=aid)
        elif db == 'BImsBoot':
            queryset = BImsBoot.objects.filter(id=aid)
        elif db == 'BImsPanel':
            queryset = BImsPanel.objects.filter(id=aid)
        elif db == 'Tms':
            queryset = Tms.objects.filter(id=aid)
        elif db == 'Epg':
            queryset = Epg.objects.filter(id=aid)
        elif db == 'Search':
            queryset = Search.objects.filter(id=aid)
        elif db == 'Pic':
            queryset = Pic.objects.filter(id=aid)
        elif db == 'Ppl':
            queryset = Ppl.objects.filter(id=aid)
        elif db == 'CosEpg':
            queryset = CosEpg.objects.filter(id=aid)
        elif db == 'Uic':
            queryset = Uic.objects.filter(id=aid)
        elif db == 'MScreen':
            queryset = MScreen.objects.filter(id=aid)
        elif db == 'DMS2':
            queryset = DMS2.objects.filter(id=aid)
        elif db == 'XMpp':
            queryset = XMpp.objects.filter(id=aid)
        elif db == 'NDms':
            queryset = NDms.objects.filter(id=aid)
        values = queryset.values('ip', 'port')[0]
        if values['port']:
            token = zabbix_token()
            port = "net.tcp.service[tcp,,%s]" % values['port']
            headers = {'Content-Type': 'application/json'}
            payload = {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    "output": "extend",
                    "host": values['ip'],
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
        response['data'] = {'z_status': z_status}
        return JsonResponse(response)
    response['code'] = 1
    response['msg'] = '请求方法不对'
    return JsonResponse(response)


@csrf_exempt
def refresh_agent(request):
    """
    刷新agent监控
    :return:
    """
    response = {
        'code': 0,
        'data': [],
        'msg': '刷新完成',
        'total': 0
    }
    if request.method == 'POST':
        body = json.loads(request.body)
        aid = body['id']
        queryset = Host.objects.filter(id=aid)
        values = queryset.values('lan_ip')[0]
        if values:
            token = zabbix_token()
            headers = {'Content-Type': 'application/json'}
            payload = {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    "output": "extend",
                    "host": values['lan_ip'],
                    "search": {
                        "key_": "agent.ping"
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
        response['data'] = {'zabbix_status': zabbix_status}
        return JsonResponse(response)
    response['code'] = 1
    response['msg'] = '请求方法不对'
    return JsonResponse(response)

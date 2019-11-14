import re
import json
import logging
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.base import View

from tabops_api.settings import DEFAULT_LOGGER, SALT_API_URL_SOUTH, SALT_API_URL_WEST
from common.views import ResponseInfo
from salt.salt_http_api import salt_api_token
from salt.salt_token_id import token_get
from asset.models import Host

logger = logging.getLogger(DEFAULT_LOGGER)


class ScanMinion(View):
    """
    salt扫描minions信息
    """
    def __init__(self):
        self.response_format = ResponseInfo().response

    def post(self, request):
        body = json.loads(request.body)
        tgt = body['saltid']
        if not re.match('SCYD-', tgt):
            self.response_format['code'] = 1
            self.response_format['msg'] = 'saltid不合规'
            return JsonResponse(self.response_format)
        # token = ''
        if "SCYD-10.1" in tgt or "SCYD-10.3" in tgt or "SCYD-west" in tgt or "SCYD-117" in tgt:
            salt_api_url = SALT_API_URL_WEST
            token = token_get("s_west", salt_api_url)
        if "SCYD-10.25" in tgt or "SCYD-172.188" in tgt or "SCYD-south" in tgt:
            salt_api_url = SALT_API_URL_SOUTH
            token = token_get("s_south", salt_api_url)
        con = Q()
        #  for scan south
        if tgt == 'SCYD-south':
            tgt = 'SCYD-*'
            q1 = Q()
            q1.connector = 'OR'
            q1.children.append(('idc', '109'))
            q1.children.append(('idc', '111'))
            q1.children.append(('idc', '210'))
            q2 = Q()
            q2.connector = 'OR'
            q2.children.append(('m_status', 1))
            con.add(q1, 'AND')
            con.add(q2, 'AND')
            Host.objects.filter(con).update(m_status=0)
        #  for scan west
        if tgt == 'SCYD-west':
            tgt = 'SCYD-*'
            q1 = Q()
            q1.connector = 'OR'
            q1.children.append(('idc', '301'))
            q1.children.append(('idc', '601'))
            q2 = Q()
            q2.connector = 'OR'
            q2.children.append(('m_status', 1))
            con.add(q1, 'AND')
            con.add(q2, 'AND')
            Host.objects.filter(con).update(m_status=0)
        logger.info('获取Minion主机资产信息')
        # result = salt_api_token({'fun': 'grains.items', 'tgt': tgt, 'expr_form': 'list'},
        #                         SALT_API_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
        result = salt_api_token({'fun': 'grains.items', 'tgt': tgt},
                                salt_api_url, {'X-Auth-Token': token}).CmdRun()['return'][0]
        logger.info('扫描Minion数量为[%s]', len(result))
        logger.debug('Minions资产信息[%s]' % result)

        for host in result:
            m_status = 1
            result[host]["ipv4"].remove('127.0.0.1')
            idc = None
            # lan_ip字段不能为空 models.py里面设置
            lan_ip = '192.168.1.2'
            man_ip = None
            for ip in result[host]["ipv4"][::-1]:
                if "10.25.172" in ip or "172.188.2" in ip:
                    idc = '109'
                    lan_ip = ip
                elif "10.25.171" in ip or "172.188.1" in ip:
                    idc = '111'
                    lan_ip = ip
                elif "172.188.3" in ip:
                    idc = '210'
                    lan_ip = ip
                if "10.1.32" in ip or "10.3.32" in ip:
                    idc = '301'
                    lan_ip = ip
                elif "10.1.33" in ip or "10.3.33" in ip:
                    idc = '601'
                    lan_ip = ip
                elif "117" in ip:
                    idc = '201'
                    lan_ip = ip
                # 南区服务器管理IP 109机房10.25.178.0, 10.110.70.0  111机房10.25.177.0, 10.110.72.0  210机房10.110.73.0
                if "10.25.178" in ip or "10.110.70" in ip or "10.25.177" in ip or "10.110.72" in ip or "10.110.73" in ip:
                    man_ip = ip
                # 西区服务器管理IP
                if "10.25.179" in ip or "10.25.181" in ip or "10.25.182" in ip or "10.25.183" in ip:
                    man_ip = ip

            rs = Host.objects.filter(salt_id=host)
            if len(rs) == 0:
                logger.info("新增主机:%s", host)
                device = Host(idc=idc,
                              salt_id=host,
                              lan_ip=lan_ip,
                              man_ip=man_ip,
                              kernel=result[host]["kernel"] if 'kernel' in result[host] else "",
                              kernel_release=result[host]["kernelrelease"] if 'kernelrelease' in result[host] else "",
                              platform=result[host]["virtual"] if 'virtual' in result[host] else "",
                              hostname=result[host]["host"] if 'host' in result[host] else "",
                              os_release=result[host]["osrelease"] if 'osrelease' in result[host] else "",
                              salt_version=result[host]["saltversion"] if 'saltversion' in result[host] else "",
                              os_finger=result[host]["osfinger"] if 'osfinger' in result[host] else "",
                              os_family=result[host]["os_family"] if 'os_family' in result[host] else "",
                              serial_number=result[host]['serialnumber'] if 'serialnumber' in result[host] else "",
                              cpu_model=result[host]["cpu_model"] if 'cpu_model' in result[host] else "",
                              product_name=result[host]['productname'] if "productname" in result[host] else "",
                              os_arch=result[host]["osarch"] if 'osarch' in result[host] else "",
                              cpu_arch=result[host]["cpuarch"] if 'cpuarch' in result[host] else "",
                              os=result[host]["os"] if 'os' in result[host] else "",
                              mem_total=result[host]["mem_total"] if 'mem_total' in result[host] else 0,
                              num_cpus=result[host]["num_cpus"] if 'num_cpus' in result[host] else 0,
                              m_status=m_status,
                              roles=result[host]["roles"][0] if 'roles' in result[host] else "",
                            )
                device.save()
            else:
                entity = rs[0]
                logger.info("更新主机:%s", entity)
                entity.idc = idc
                entity.lan_ip = lan_ip
                entity.man_ip = man_ip
                entity.kernel = result[host]["kernel"] if 'kernel' in result[host] else ""
                entity.kernel_release = result[host]["kernelrelease"] if 'kernelrelease' in result[host] else ""
                entity.platform = result[host]["virtual"] if 'virtual' in result[host] else ""
                entity.hostname = result[host]["host"] if 'host' in result[host] else ""
                entity.os_release = result[host]["osrelease"] if 'osrelease' in result[host] else ""
                entity.salt_version = result[host]["saltversion"] if 'saltversion' in result[host] else ""
                entity.os_finger = result[host]["osfinger"] if 'osfinger' in result[host] else ""
                entity.os_family = result[host]["os_family"] if 'os_family' in result[host] else ""
                entity.serial_number = result[host]["serialnumber"] if 'serialnumber' in result[host] else ""
                entity.cpu_model = result[host]["cpu_model"] if 'cpu_model' in result[host] else ""
                entity.product_name = result[host]["productname"] if 'productname' in result[host] else ""
                entity.os_arch = result[host]["osarch"] if 'osarch' in result[host] else ""
                entity.cpu_arch = result[host]["cpuarch"] if 'cpuarch' in result[host] else ""
                entity.os = result[host]["os"] if 'os' in result[host] else ""
                entity.mem_total = result[host]["mem_total"] if 'mem_total' in result[host] else 0
                entity.num_cpus = result[host]["num_cpus"] if 'num_cpus' in result[host] else 0
                entity.m_status = m_status
                entity.roles = result[host]["roles"][0] if 'roles' in result[host] else ""
                entity.save()
                self.response_format['data'] = {"idc": entity.idc,
                                                "lan_ip": entity.lan_ip,
                                                "man_ip": entity.man_ip,
                                                "platform": entity.platform,
                                                "hostname": entity.hostname,
                                                "salt_version": entity.salt_version,
                                                "os_finger": entity.os_finger,
                                                "serial_number": entity.serial_number,
                                                "num_cpus": entity.num_cpus,
                                                "mem_total": entity.mem_total,
                                                "roles": entity.roles,
                                                "minion_status": "Up"}
        self.response_format['total'] = len(result)
        return JsonResponse(self.response_format)

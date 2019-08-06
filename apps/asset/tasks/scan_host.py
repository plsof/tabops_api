import re
import logging
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

from tabops_api.settings import DEFAULT_LOGGER, SALT_API_URL
from salt.salt_http_api import salt_api_token
from salt.salt_token_id import token_id
from asset.models import Host

logger = logging.getLogger(DEFAULT_LOGGER)


# @csrf_exempt
def scan_host(request):
    """
    扫描客户端信息
    :return:
    """
    if request.method == 'GET':
        response = {
            'code': 0,
            'data': [],
            'msg': '扫描完成',
            'total': 0
        }
        # tgt = request.POST.get('saltid', '')
        tgt = request.GET.get('saltid')
        if not re.match('SCYD-', tgt):
            response['code'] = 1
            response['msg'] = 'saltid不合规'
            return JsonResponse(response)
        logger.info('获取Minion主机资产信息')
        # result = salt_api_token({'fun': 'grains.items', 'tgt': tgt, 'expr_form': 'list'},
        #                         SALT_API_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
        result = salt_api_token({'fun': 'grains.items', 'tgt': tgt},
                                SALT_API_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
        logger.info('扫描Minion数量为[%s]', len(result))
        logger.debug('Minions资产信息[%s]' % result)

        #  for scan all
        if tgt == 'SCYD-*':
            Host.objects.filter(m_status=0).update(m_status=1)

        for host in result:
            m_status = 0
            result[host]["ipv4"].remove('127.0.0.1')
            idc = None
            # lan_ip 不能为空
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
                # 109机房管理IP
                if "10.25.178" in ip or "10.110.70" in ip:
                    man_ip = ip
                # 111机房管理IP
                elif "10.25.177" in ip or "10.110.72" in ip:
                    man_ip = ip
                # 210机房管理IP
                elif "10.110.73" in ip:
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

        response['total'] = len(result)
        return JsonResponse(response)

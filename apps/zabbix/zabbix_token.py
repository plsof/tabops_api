from django.core.cache import cache

from .zabbix_api import zabbix_api


def zabbix_token():
    z_token = cache.get("z_token")
    if z_token == None:
        res = zabbix_api()
        if res != 1:
            z_token = res
            cache.set("z_token", z_token, timeout=12*60*60)
        else:
            return 1
    return z_token

import json
import requests
import logging
from django.core.cache import cache

from tabops_api.settings import DEFAULT_LOGGER, ZABBIX_USER, ZABBIX_PASSWORD

logger = logging.getLogger(DEFAULT_LOGGER)

PAYLOAD = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": ZABBIX_USER,
                "password": ZABBIX_PASSWORD
            },
            "id": 1
        }

HEADERS = {'Content-Type': 'application/json'}


def token_get(region, zabbix_api_url):
    token = cache.get(region)
    if token is None:
        try:
            ret = requests.post(zabbix_api_url, data=json.dumps(PAYLOAD), headers=HEADERS, timeout=5, verify=False)
            res = json.loads(ret.text)
            token = res["result"]
            cache.set(region, token, timeout=12 * 60 * 60)
        except requests.ConnectionError as e:
            logger.error("zabbix认证失败%s" % e)
    return token

import json
import requests
import logging
from django.core.cache import cache

from tabops_api.settings import DEFAULT_LOGGER, ZABBIX_API_URL_SOUTH, ZABBIX_API_URL_WEST, ZABBIX_USER, ZABBIX_PASSWORD

logger = logging.getLogger(DEFAULT_LOGGER)

headers = {'Content-Type': 'application/json'}


def zabbix_api_south():
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_USER,
            "password": ZABBIX_PASSWORD
        },
        "id": 1
    }
    try:
        ret = requests.post(ZABBIX_API_URL_SOUTH, data=json.dumps(payload), headers=headers, timeout=5, verify=False)
    except requests.ConnectionError as e:
        logging.error(e)
        return 1
    res = json.loads(ret.text)
    return res["result"]


def zabbix_api_west():
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_USER,
            "password": ZABBIX_PASSWORD
        },
        "id": 1
    }
    try:
        ret = requests.post(ZABBIX_API_URL_WEST, data=json.dumps(payload), headers=headers, timeout=5, verify=False)
    except requests.ConnectionError as e:
        logging.error(e)
        return 1
    res = json.loads(ret.text)
    return res["result"]


def zabbix_token_south():
    z_token_south = cache.get("z_token_south")
    if z_token_south is None:
        res = zabbix_api_south()
        if res != 1:
            z_token_south = res
            cache.set("z_token_south", z_token_south, timeout=12*60*60)
        else:
            return 1
    return z_token_south


def zabbix_token_west():
    z_token_west = cache.get("z_token_west")
    if z_token_west is None:
        res = zabbix_api_west()
        if res != 1:
            z_token_west = res
            cache.set("z_token_west", z_token_west, timeout=12*60*60)
        else:
            return 1
    return z_token_west

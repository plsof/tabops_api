import json
import requests
import logging

from tabops_api.settings import DEFAULT_LOGGER, ZABBIX_API_URL, ZABBIX_USER, ZABBIX_PASSWORD

logger = logging.getLogger(DEFAULT_LOGGER)

headers = {'Content-Type': 'application/json'}

def zabbix_api():
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
        ret = requests.post(ZABBIX_API_URL, data=json.dumps(payload), headers=headers, timeout=5, verify=False)
    except requests.ConnectionError as e:
        logging.error(e)
        return 1
    res = json.loads(ret.text)
    return res["result"]


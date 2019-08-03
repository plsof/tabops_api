import sys
import logging


from tabops_api.settings import DEFAULT_LOGGER, SALT_USER, SALT_PASSWORD, SALT_API_URL
from .salt_http_api import salt_api_token

logger = logging.getLogger(DEFAULT_LOGGER)


def token_id():
    s = salt_api_token(
        {
            "username": SALT_USER,
            "password": SALT_PASSWORD,
            "eauth": "pam"
        },
        SALT_API_URL + "login",
        {}
    )
    try:
        rs = s.run()
    except Exception as e:
        logger.error("salt_api认证失败")
        sys.exit()
    return rs["return"][0]["token"]

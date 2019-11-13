import logging
from django.core.cache import cache

from tabops_api.settings import DEFAULT_LOGGER, SALT_USER, SALT_PASSWORD
from .salt_http_api import salt_api_token

logger = logging.getLogger(DEFAULT_LOGGER)


def token_get(region, salt_api_url):
    token = cache.get(region)
    if token is None:
        s = salt_api_token(
            {
                "username": SALT_USER,
                "password": SALT_PASSWORD,
                "eauth": "pam"
            },
            salt_api_url + "login",
            {}
        )
        try:
            rs = s.run()
            token = rs["return"][0]["token"]
            cache.set(region, token, timeout=12 * 60 * 60)
        except Exception as e:
            logger.error("salt_api认证失败%s" % e)
    return token

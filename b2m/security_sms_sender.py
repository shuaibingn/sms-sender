import logging
import time

import requests

from config.b2m import b2m_config
from pkg.aes import AESCipher
from pkg.phone_number import parse_phone_number

try:
    import simplejson as json
except ImportError:
    import json


def __send_by_em(to, content, message_type):
    to = parse_phone_number(to)
    if not to:
        logging.error(f"invalid phone number {to}")
        return

    config = b2m_config.get(message_type)
    url, app_id, secret = config.get("url"), config.get("app_id"), config.get("secret")
    request_body = {
        "mobile": to,
        "content": content,
        "requestTime": int(time.time() * 1000),
        "requestValidPeriod": 30
    }
    headers = {
        "appId": app_id,
    }

    aes = AESCipher(secret)
    encrypt_data = aes.encrypt(json.dumps(request_body))

    try:
        response = requests.post(url, headers=headers, data=encrypt_data)
    except Exception as e:
        logging.error(f"send sms by em to {to}, error {e}")
        return

    response.encoding = "utf-8"
    response_result = response.headers.get("result")
    if response_result != "SUCCESS":
        logging.error(f"send sms by em to {to} error")
        return

    decrypt_data = aes.decrypt(response.content)
    logging.info(f"send sms by em to {to} success, response {decrypt_data}")

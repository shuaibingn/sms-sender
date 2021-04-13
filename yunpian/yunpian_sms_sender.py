import logging

from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient

from config.yunpian import yunpian_config

api_key = yunpian_config.get("api_key")


def send_by_yunpian(to, content):
    logging.info('sending sms by yunpian to :{} content: {}'.format(to, content))

    clnt = YunpianClient(apikey=api_key)
    param = {YC.MOBILE: to, YC.TEXT: content}
    r = clnt.sms().single_send(param)
    logging.info(
        'sending sms {} result: {} {}, {}, {}, {}'.format(to, r.code(), r.msg(), r.data(), r.detail(), r.exception()))


def send_voice_by_yunpian(to, code):
    clnt = YunpianClient(apikey=api_key)
    param = set_params(to, code)
    r = clnt.voice().send(param)
    return r


def set_params(to: str, code: str):
    """
    设置语音验证码语言
    https://www.yunpian.com/official/document/sms/zh_CN/voicecode_list

    zh	中文      验证码是1-2-3-4
    en	英文      Your verification code is 1-2-3-4
    id	印尼语    Kode verifikasi Anda adalah 1-2-3-4
    vi	越南语	 Mã xác minh của bạn là 1-2-3-4
    tr	土耳其语	 Doğrulama kodunuz 1-2-3-4
    ru	俄语	     Ваш проверочный код 1-2-3-4
    de	德语	     Ihr Bestätigungscode lautet 1-2-3-4
    fr	法语	     Votre code de vérification est 1-2-3-4
    it	意大利语	 Il tuo codice di verifica è 1-2-3-4
    pt	葡萄牙语	 O seu código de verificação é 1-2-3-4
    """
    param = {YC.MOBILE: to, YC.CODE: code}
    # 台湾用户语音验证码为中文
    if to.startswith("+886"):
        param["language"] = "zh"

    return param

numbers = ["886"]


def parse_phone_number(phone_number):
    # 国内号码不按照国际号码方式处理，直接返回手机号，这样亿美才能发送成功
    if phone_number.startswith("+86"):
        return phone_number[3:]

    real_phone_number = None
    for number in numbers:
        p = "+" + number

        if phone_number.startswith(p + "0"):
            real_phone_number = phone_number[len(p) + 1:]

        elif phone_number.startswith(p):
            real_phone_number = phone_number[len(p):]

        if real_phone_number:
            return "00" + number + real_phone_number

    return None

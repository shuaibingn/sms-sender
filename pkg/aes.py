from Crypto.Cipher import AES


class AESCipher:

    def __init__(self, secret_key):
        self.__encrypt_key = secret_key

    def encrypt(self, data):
        BS = AES.block_size
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        cipher = AES.new(self.__encrypt_key, AES.MODE_ECB)
        encrypt_data = cipher.encrypt(pad(data))
        return encrypt_data

    def decrypt(self, encrypt_data):
        unpad = lambda s: s[0:-s[-1]]
        cipher = AES.new(self.__encrypt_key, AES.MODE_ECB)
        decrData = unpad(cipher.decrypt(encrypt_data))
        return decrData.decode('utf-8')

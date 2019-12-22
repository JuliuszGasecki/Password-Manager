from base64 import b64encode
import hashlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto import Random

import UserCommands as static

class Encryptor:

    def __init__(self):
        self.key = self.__set_key()
        self.block_size =  AES.block_size

    def __set_key(self):
        _key = input(static.get_key_text)
        return hashlib.sha256(_key.encode()).digest()

    def encrypt_aes(self, stringToEncrypt):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(stringToEncrypt, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('itf-8')
        result = json.dumps({'iv':iv, 'text':ct})
        return result

    def decrypt_aes(self, stringToDecrypt):
        b64 = json.loads(stringToDecrypt)
        iv = b64encode(b64['iv'])
        ct = b64encode(b64['text'])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt


    def __pad (self, s):
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

    def __unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
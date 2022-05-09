import string
import base64
from Clases.Stamp.EncrypterObjAction import EncrypterObjAction


class EncrypterObj(EncrypterObjAction):
    __result: string

    @property
    def get_result(self):
        return self.__result

    def __init__(self):
        self.__result = ""

    def encrypt_data(self, data: string):
        self.__result = base64.b64encode(str(data).encode('UTF-8')).decode('UTF-8')
        return self.__result

    def dencrypt_data(self, data: string):
        self.__result = base64.b64decode(str(data).encode('UTF-8')).decode('UTF-8')
        return self.__result


import string


class Issuers(object):
    __CN: string
    __C: string
    __ST: string
    __L: string
    __O: string
    __OU: string
    __email_address: string

    def __init__(self):
        self.__CN = "SGIED-CERT"
        self.__C = "MEXICO"
        self.__ST = "CDMX"
        self.__L = "UPIITA"
        self.__O = "IPN"
        self.__OU = "sgied.com.mx"
        self.__email_address = ""

    @property
    def get_cn(self):
        return self.__CN

    @property
    def get_c(self):
        return self.__C

    @property
    def get_st(self):
        return self.__ST

    @property
    def get_l(self):
        return self.__L

    @property
    def get_o(self):
        return self.__O

    @property
    def get_ou(self):
        return self.__OU

    @property
    def email_address(self):
        return self.__email_address

import string

from OpenSSL import crypto
from Clases.Stamp.StamperAction import StamperAction
from Clases.Stamp.IssuerObj import Issuers
from Clases.Stamp.EncrypterObj import EncrypterObj
from Clases.Users.ClassMate import ClassMate


class Stamper(StamperAction):
    __subject: ClassMate
    __issuer: Issuers
    __serial_number: int
    __certifier: crypto.X509
    __TIME_SIGN_VALID: int
    __NOT_AFTER: int = 0
    __cert: bytes
    __key: bytes

    def __init__(self, subject: ClassMate, serial_number: int, extended_time: int):
        self.__certifier = crypto.X509()
        self.__subject = subject
        self.__issuer = Issuers()
        self.__serial_number = serial_number
        self.__TIME_SIGN_VALID = (24 * 60 * 60 * extended_time, 24 * 60 * 60 * 365 * 5)[extended_time == 0]

    def make_signs(self):
        keypair: crypto.PKey = crypto.PKey()
        keypair.generate_key(crypto.TYPE_RSA, 4096)
        self.__certifier.set_version(2)
        # For subject
        en: EncrypterObj = EncrypterObj()
        cn: string = \
            str(self.subject.get_mate_id) + "-" + self.__subject.get_mate_names + "-" + \
            self.__subject.get_mate_ape_pat + "-" + self.__subject.get_mate_ape_mat
        self.__certifier.get_subject().CN = en.encrypt_data(cn)
        self.__certifier.get_subject().ST = self.__issuer.get_st
        self.__certifier.get_subject().__setattr__("L", self.__issuer.get_l)
        self.__certifier.get_subject().__setattr__("O", self.__issuer.get_o)
        self.__certifier.get_subject().OU = en.encrypt_data(self.__subject.get_user_area_school.get_area_name)
        self.__certifier.get_subject().emailAddress = \
            en.encrypt_data(self.__subject.get_mate_contact.get_con_email.get_email_subject)
        # For issuer
        self.__certifier.get_issuer().CN = self.__issuer.get_cn
        self.__certifier.get_issuer().ST = self.__issuer.get_st
        self.__certifier.get_issuer().__setattr__("L", self.__issuer.get_l)
        self.__certifier.get_issuer().__setattr__("O", self.__issuer.get_o)
        self.__certifier.get_issuer().OU = self.__issuer.get_ou
        # For continues certificate
        self.__certifier.set_serial_number(self.__serial_number)
        self.__certifier.gmtime_adj_notAfter(self.__TIME_SIGN_VALID)
        self.__certifier.gmtime_adj_notBefore(self.__NOT_AFTER)
        self.__certifier.set_pubkey(keypair)
        self.__certifier.sign(keypair, 'sha256')
        self.__cert = crypto.dump_certificate(crypto.FILETYPE_PEM, self.__certifier)
        self.__key = crypto.dump_privatekey(crypto.FILETYPE_PEM, keypair)

    def save_signs(self):
        var = {
            "cert": "cert" + str(self.__subject.get_mate_id) + ".pem",
            "key": "key" + str(self.__subject.get_mate_id) + ".pem"
        }
        cert = open(var["cert"], "w")
        cert.write(self.__cert.decode('utf-8'))
        cert.close()
        key = open(var["key"], "w")
        key.write(self.__key.decode('utf-8'))
        key.close()
        return var

    @property
    def subject(self):
        return self.__subject

    @property
    def issuer(self):
        return self.__issuer

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def time_sign_valid(self):
        return self.__TIME_SIGN_VALID

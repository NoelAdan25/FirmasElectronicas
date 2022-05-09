import string
from Clases.Email.Emails import Email
from Clases.Users.User import User
from Clases.School.School import SchoolAreas


class Sex:
    __sex_id: int
    __sex_desc: string

    def __init__(self, class_sex: {}):
        self.__sex_id = int(class_sex["sex_id"])
        self.__sex_desc = class_sex["sex_desc"]

    @property
    def get_id_sex(self):
        return self.__sex_id

    @property
    def get_sex_desc(self):
        return self.__sex_desc


class Contact:
    __con_id: int
    __con_tel: string
    __con_tel_landline: string
    __con_email: Email

    def __init__(self, class_contact: {}):
        self.__con_id = int(class_contact["con_id"])
        self.__con_tel = class_contact["con_tel"]
        self.__con_tel_landline = class_contact["con_landline"]
        self.__con_email = Email(class_contact["con_email"]["ema_subject"])

    @property
    def get_con_id(self):
        return self.__con_id

    @property
    def get_con_tel(self):
        return self.__con_tel

    @property
    def get_con_tel_landline(self):
        return self.__con_tel_landline

    @property
    def get_con_email(self):
        return self.__con_email


class ClassMate:
    __mate_id: int
    __mate_names: string
    __mate_ape_pat: string
    __mate_ape_mat: string
    __mate_sex: Sex
    __mate_contact: Contact
    __mate_user: User
    __mate_area_school: SchoolAreas

    def __init__(self, class_mate: {}):
        self.__mate_id = int(class_mate["mate_id"])
        self.__mate_names = class_mate["mate_names"]
        self.__mate_ape_pat = class_mate["mate_ape_pat"]
        self.__mate_ape_mat = class_mate["mate_ape_mat"]
        self.__mate_sex = Sex(class_mate["mate_sex"])
        self.__mate_contact = Contact(class_mate["mate_contact"])
        self.__mate_user = User(class_mate["mate_user"])
        self.__mate_area_school = SchoolAreas(class_mate["mate_area"])

    @property
    def get_mate_id(self):
        return self.__mate_id

    @property
    def get_mate_names(self):
        return self.__mate_names

    @property
    def get_mate_ape_pat(self):
        return self.__mate_ape_pat

    @property
    def get_mate_ape_mat(self):
        return self.__mate_ape_mat

    @property
    def get_mate_sex(self):
        return self.__mate_sex

    @property
    def get_mate_contact(self):
        return self.__mate_contact

    @property
    def get_con_user(self):
        return self.__mate_user

    @property
    def get_user_area_school(self):
        return self.__mate_area_school

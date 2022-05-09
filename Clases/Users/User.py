import string
from Clases.Users.UserActions import UserAction


class User(UserAction):
    __user_id: int
    __user_name: string
    __user_pass: string

    def __init__(self, class_user: {}):
        self.__user_pass = class_user["user_pass"]
        self.__user_name = class_user["user_name"]
        self.__user_id = class_user["user_id"]

    @property
    def get_user_id(self):
        return self.__user_id

    @property
    def get_user_name(self):
        return self.__user_name

    @property
    def get_user_pass(self):
        return self.__user_pass

    def is_exists(self, user_name: string, user_pass: string):
        # We check if exists a user associated to the classmate created
        return True

    def update_user_info(self):
        return "Updating"

    def insert_user_info(self):
        return "Inserting"

    def is_valid_user_info(self):
        return False
